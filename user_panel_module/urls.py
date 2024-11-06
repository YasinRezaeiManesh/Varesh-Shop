from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserPanelPageView.as_view(), name='user_panel'),
    path('edit-profile', views.EditUserProfilePageView.as_view(), name='edit_profile'),
    path('change-pass', views.ChangePasswordPageView.as_view(), name='change_password'),
    path('tickets', views.tickets, name='tickets'),
    path('user-basket', views.user_basket, name='user_basket'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail'),
    path('change-order-detail-count', views.change_order_detail_count, name='change_order_detail_count'),
    path('404_page', views.not_found_page, name='404_page'),
]
