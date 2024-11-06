from django.shortcuts import render
from django.views.generic import ListView, DetailView
from service_module.models import Service, ServiceCategory
from site_module.models import SiteQuestions


# Create your views here.


class ServiceView(ListView):
    template_name = 'service_module/service_list.html'
    model = Service

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['service'] = Service.objects.filter()
        return context


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_module/service_detail.html'

    def get_context_data(self, **kwargs):
        loaded_service = self.object
        context = super().get_context_data(**kwargs)
        context['questions_list'] = SiteQuestions.objects.all()
        context['service_list'] = Service.objects.filter()
        context['related_service'] = Service.objects.filter(tags_id=loaded_service.tags_id).exclude(pk=loaded_service.id)
        return context
