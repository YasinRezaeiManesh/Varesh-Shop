from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.ContactUs)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'is_read_by_admin', 'title']
