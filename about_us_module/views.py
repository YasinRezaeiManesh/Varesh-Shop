from django.shortcuts import render
from django.views.generic.base import TemplateView
from about_us_module.models import AboutUs


# Create your views here.


class AboutUsView(TemplateView):
    template_name = 'about_us_module/about_us_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'about_us': AboutUs.objects.all().first()
        }
        return context
