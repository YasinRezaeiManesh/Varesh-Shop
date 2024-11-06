from django.urls import path
from order_module import views

urlpatterns = [
    path('add-to-order', views.add_product_to_order, name='add_product_to_order'),
    path('continue-payment', views.continue_payment, name='continue_payment'),
]
