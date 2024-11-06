from django.shortcuts import render
from . import models
from django.views.generic import ListView, TemplateView

# Create your views here.


class QuestionListView(ListView):
    model = models.SiteQuestions
    context_object_name = 'questions_list'
    template_name = 'site_module/question_page.html'


class CertificateListView(ListView):
    model = models.SiteCertificate
    context_object_name = 'certificate_list'
    template_name = 'site_module/certificate_page.html'
    paginate_by = 6


class TeamListView(ListView):
    model = models.SiteTeam
    context_object_name = 'team_list'
    template_name = 'site_module/team_page.html'
    paginate_by = 8
