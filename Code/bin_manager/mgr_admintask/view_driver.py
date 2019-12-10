from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)
from django.urls import reverse_lazy, reverse

from mgr_database.models import  TruckDriver


class createTruckDriver(CreateView):
    template_name = 'create.html'
    model = TruckDriver
    success_url = '/admin/success/'
    fields = '__all__'
