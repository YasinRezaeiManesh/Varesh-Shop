from django.shortcuts import render, redirect
from .forms import ContactModelForm
from django.views.generic.edit import CreateView

# Create your views here.


class ContactUsView(CreateView):
    form_class = ContactModelForm
    template_name = 'contact_us_module/contact_us.html'
    success_url = '/contact-us/'
