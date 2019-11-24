from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView)
from mgr_database.models import RequestDetail


class AdminIndex(TemplateView):
    template_name = 'base_admin.html'