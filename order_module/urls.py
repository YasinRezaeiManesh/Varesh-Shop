from django.urls import path
from order_module import views

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add_product_to_order'),
    path('continue-payment', views.continue_payment, name='continue_payment'),
    path('request-payment/', views.request_payment, name='request_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
]
