from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'inventory', 'is_active']


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


@admin.register(models.ProductTags)
class ProductTagsAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


@admin.register(models.ProductComment)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'shamsi_date', 'parent']
