from itertools import product

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView, ListView
from account_module.models import User
from product_module.models import Product, ProductCategory, ProductComment


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 8

    def get_queryset(self):
        query = super().get_queryset()
        category_name = self.kwargs.get('category')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product: Product = kwargs.get('object')
        context['comments'] = ProductComment.objects.filter(product_id=product.id, parent=None).order_by('-shamsi_date').prefetch_related('productcomment_set')
        context['comments_count'] = ProductComment.objects.filter(product_id=product.id).count()
        context['related_products'] = Product.objects.filter(tags_id=product.tags.id).exclude(pk=product.id)[:4]
        return context


def product_category_component(request):
    context = {
        'main_categories': ProductCategory.objects.filter(is_active=True),
    }
    return render(request, 'product_module/components/producct_category_component.html', context)


def add_product_comment(request):
    if request.user.is_authenticated:
        product_id = request.GET.get('product_id')
        product_comment = request.GET.get('productComment')
        parent_id = request.GET.get('parent_id')
        new_comment = ProductComment(product_id=product_id, text=product_comment, user_id=request.user.id, parent_id=parent_id)
        new_comment.save()

        context = {
            'comments': ProductComment.objects.filter(product_id=product_id, parent=None).order_by('-shamsi_date').prefetch_related('productcomment_set'),
            'comments_count': ProductComment.objects.filter(product_id=product_id).count()
        }

        return render(request, 'product_module/include/product_comment_partial.html', context)

    return HttpResponse('by')
