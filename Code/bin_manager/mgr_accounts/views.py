from django.shortcuts import render

from django.views.generic import (TemplateView, DetailView)
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'

class ProfileView(DetailView):
    template_name ='account_profile.html'