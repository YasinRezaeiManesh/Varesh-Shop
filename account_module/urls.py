from django.urls import path
from . import views


urlpatterns = [
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('forget-password', views.ForgotPasswordView.as_view(), name='forget_password'),
    path('reset-password/<active_code>', views.ResetPasswordView.as_view(), name='reset_password')
]