from mgr_admintask.forms import TripForm
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)


class CreateTripView(FormView):
    template_name = 'create.html'
    form_class = TripForm
    success_url = '/admin/success/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
