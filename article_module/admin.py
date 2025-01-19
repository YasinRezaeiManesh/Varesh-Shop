from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'shamsi_date']


@admin.register(models.ArticleCategory)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_delete']


@admin.register(models.ArticleTags)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']


@admin.register(models.ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ["user", "article", "success", "parent"]
