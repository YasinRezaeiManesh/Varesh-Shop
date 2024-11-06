from django.contrib.auth import logout
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView
from account_module.models import User
from order_module.models import Order, OrderDetail
from .forms import EditProfileModelForm, ChangePasswordForm
from contact_us_module.models import ContactUs


# Create your views here.

class UserPanelPageView(TemplateView):
    template_name = 'user_panel_module/panel_page.html'


class EditUserProfilePageView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            current_user = User.objects.filter(id=request.user.id).first()
            edit_form = EditProfileModelForm(instance=current_user)
            context = {
                'form': edit_form,
                'current_user': current_user,
            }
            return render(request, 'user_panel_module/edit_profile_page.html', context)

        return redirect(reverse('404_page'))

    def post(self, request: HttpRequest):
        if request.user.is_authenticated:
            current_user = User.objects.filter(id=request.user.id).first()
            edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
            if edit_form.is_valid():
                edit_form.save(commit=True)
            context = {
                'form': edit_form,
                'current_user': current_user,
            }
            return render(request, 'user_panel_module/edit_profile_page.html', context)

        return redirect(reverse('404_page'))


class ChangePasswordPageView(View):
    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            form = ChangePasswordForm()
            context = {
                'form': form,
            }
            return render(request, 'user_panel_module/change_password_page.html', context)

        return redirect(reverse('404_page'))

    def post(self, request: HttpRequest):
        if request.user.is_authenticated:
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                current_user = User.objects.filter(id=request.user.id).first()
                if current_user.check_password(form.cleaned_data.get('current_password')):
                    current_user.set_password(form.cleaned_data.get('password'))
                    current_user.save()
                    logout(request)
                    return redirect(reverse('login'))
                else:
                    form.add_error('current_password', 'کلمه عبور وارد شده اشتباه میباشد')

            context = {
                'form': form,
            }
            return render(request, 'user_panel_module/change_password_page.html', context)

        return redirect(reverse('404_page'))


def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel_module/components/user_panel_menu_component.html', {})


def tickets(request: HttpRequest):
    if request.user.is_authenticated:
        user = User.objects.filter(id=request.user.id).first()
        user_tickets = ContactUs.objects.filter(email__iexact=request.user.email)
        context = {
            'user_tickets': user_tickets,
            'user': user
        }
        return render(request, 'user_panel_module/tickets.html', context)

    return redirect(reverse('404_page'))


def not_found_page(request: HttpRequest):
    return render(request, 'site_module/include/404_page.html')


def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel_module/user_basket.html', context)


def remove_order_detail(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not found detail id'
        })

    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id, order__is_paid=False).delete()
    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail not found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })


def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None:
        return JsonResponse({
            'status': 'not found detail or state'
        })
    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id, order__is_paid=False).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'not found detail'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel_module/user_basket_content.html', context)
    })
