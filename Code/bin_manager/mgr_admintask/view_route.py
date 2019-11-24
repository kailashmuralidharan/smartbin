from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)
from django.urls import reverse_lazy, reverse


from mgr_database.models import  Route


class createRoute(CreateView):
    template_name = 'create.html'
    model = Route
    success_url = '/admin/success/'
    fields = '__all__'

class listRoute(ListView):
    model = Route
    template_name = 'list_route.html'
    context_object_name = 'list_route'

class updateRoute(UpdateView):
    fields = ("route_id","route_name",)
    template_name = 'create.html'
    model = Route
    success_url = reverse_lazy('admintask:list_route')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Route, route_id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class deleteRoute(DeleteView):
    model = Route
    success_url = reverse_lazy('admintask:list_route')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Route, route_id = id_)
