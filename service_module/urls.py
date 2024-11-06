from django.urls import path
from . import views


urlpatterns = [
    path('', views.ServiceView.as_view(), name='service_list'),
    path('<slug:slug>', views.ServiceDetailView.as_view(), name='service_detail'),
]
