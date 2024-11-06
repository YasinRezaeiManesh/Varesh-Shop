from django.shortcuts import render
from django.views.generic.base import TemplateView
from product_module.models import Product
from site_module.models import SiteSettings, SiteQuestions
from about_us_module.models import AboutUs
from service_module.models import Service
from utils.convertors import group_list


# Create your views here.


class HomeView(TemplateView):
    template_name = 'home_module/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'questions_list': SiteQuestions.objects.all(),
            'about_us': AboutUs.objects.all().first(),
            'services': Service.objects.all()[:3],
            'products': Product.objects.filter(is_active=True)[:4],
        }
        return context


def site_header_component(request):
    site_settings: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
    context = {
        'site_settings': site_settings,
    }

    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    site_settings: SiteSettings = SiteSettings.objects.filter(is_main_setting=True).first()
    context = {
        'site_settings': site_settings,
    }

    return render(request, 'shared/site_footer_component.html', context)

