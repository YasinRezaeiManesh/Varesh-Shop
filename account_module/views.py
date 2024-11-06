from django.http import Http404, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import forms
from .models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from utils.email_service import send_email


# Create your views here.


class RegisterView(View):
    def get(self, request):
        register_form = forms.RegisterForm()
        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            user_first_name = register_form.cleaned_data.get('first_name')
            user_last_name = register_form.cleaned_data.get('last_name')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()

            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری میباشد')
            else:
                new_user = User(
                    email=user_email,
                    email_active_code=get_random_string(48),
                    username=user_email,
                    is_active=True,
                    first_name=user_first_name,
                    last_name=user_last_name,
                )
                new_user.set_password(user_password)
                new_user.save()

                return redirect(reverse('login'))

        context = {
            'register_form': register_form,
        }
        return render(request, 'account_module/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = forms.LoginForm
        context = {
            'login_form': login_form,
        }
        return render(request, 'account_module/login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()

            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    is_password_current = user.check_password(user_password)
                    if is_password_current:
                        login(request, user)
                        return redirect(reverse('home_page'))
                    else:
                        login_form.add_error('email', 'کلمه عبور اشتباه است')
            else:
                login_form.add_error('email', 'حساب کاربری شما فعال نشده است')

        context = {
            'login_form': login_form,
        }
        return render(request, 'account_module/login_page.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class ForgotPasswordView(View):
    def get(self, request: HttpRequest):
        forget_password_form = forms.ForgetPasswordForm()
        context = {
            'forget_password_form': forget_password_form,
        }
        return render(request, 'account_module/forget_password.html', context)

    def post(self, request: HttpRequest):
        forget_password_form = forms.ForgetPasswordForm(request.POST)
        if forget_password_form.is_valid():
            user_email = forget_password_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'email/forgot_password.html')

                return redirect(reverse('home_page'))


class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login'))

        reset_password_form = forms.ResetPasswordForm()
        context = {
            'reset_password_form': reset_password_form,
            'user': user,
        }

        return render(request, 'account_module/reset_password.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_password_form = forms.ResetPasswordForm(request.POST)
        if reset_password_form.is_valid():
            user: User = User.objects.filter(email_active_code__iexact=active_code).first()
            if user is None:
                return redirect(reverse('login'))

            user_new_password = reset_password_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(48)
            user.is_active = True
            user.save()
            return redirect(reverse('login'))
