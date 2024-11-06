from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SiteQuestions)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['question']


@admin.register(models.SiteCertificate)
class SiteCertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'name']


@admin.register(models.SiteTeam)
class SiteTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'job']
