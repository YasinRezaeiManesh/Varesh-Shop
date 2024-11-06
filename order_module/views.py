from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from order_module.models import Order, OrderDetail
from product_module.models import Product
from site_module.models import SiteSettings


# Create your views here.


def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    product_count = int(request.GET.get('count'))

    if product_count < 1:
        return JsonResponse({
            'status': 'invalid count',
            'text': 'مقدار وارد شده نامعبتر میباشد',
            'title': 'خطا',
            'icon': 'error',
            'confirm_button_text': 'باشه ، ممنون',
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
            current_order_detail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += product_count
                current_order_detail.save()
            else:
                new_order_detail = OrderDetail(order_id=current_order.id, product_id=product_id, count=product_count)
                new_order_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما افزوده شد',
                'title': 'عملیات موفقیت آمیز بود',
                'icon': 'success',
                'confirm_button_text': 'باشه ، ممنون',
            })
        else:
            return JsonResponse({
                'status': 'not found',
                'text': 'محصول مورد نظر پیدا نشد',
                'title': 'خطا',
                'icon': 'error',
                'confirm_button_text': 'باشه ، ممنون',
            })

    return JsonResponse({
        'status': 'user is not authenticated',
        'text': 'لطفا در ابتدا وارد حساب کاربری خود در وبسایت شوید',
        'title': 'خطا',
        'icon': 'error',
        'confirm_button_text': 'ورود به حساب کاربری',
    })


def continue_payment(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total()

    context = {
        'order': current_order,
        'sum': total_amount,
        'site': SiteSettings.objects.all().first()
    }
    return render(request, 'order_module/continue_payment.html', context)
