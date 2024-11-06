from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.ServiceCategory)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


@admin.register(models.ServiceTags)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title']
