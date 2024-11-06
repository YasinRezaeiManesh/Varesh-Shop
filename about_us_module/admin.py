from django.contrib import admin

from about_us_module.models import AboutUs


# Register your models here.


@admin.register(AboutUs)
class AboutUsModuleAdmin(admin.ModelAdmin):
    pass
