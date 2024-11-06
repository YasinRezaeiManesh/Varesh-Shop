from django.urls import path
from . import views


urlpatterns = [
    path('questions', views.QuestionListView.as_view(), name='questions'),
    path('certificates', views.CertificateListView.as_view(), name='certificates'),
    path('team', views.TeamListView.as_view(), name='team'),
]
