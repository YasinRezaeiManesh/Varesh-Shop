from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='products_detail'),
    path('product-comment/', views.add_product_comment, name='product_comment'),
    path('cat/<str:category>', views.ProductListView.as_view(), name='product_category'),
]