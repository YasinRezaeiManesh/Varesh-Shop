from django.contrib import admin

from order_module.models import Order, OrderDetail


# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_paid', 'payment_date']


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order']
