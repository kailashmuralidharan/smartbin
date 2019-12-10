from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)
from django.urls import reverse_lazy, reverse


from mgr_database.models import  RequestDetail, Route, Account


class createRequest(CreateView):
    template_name = 'createUser.html'
    model = RequestDetail
    #success_url = '/admin/success/'
    fields = ("request_id","request_type","pickup_date",)

class viewRequests(ListView):
    model = RequestDetail
    template_name = 'view_requests.html'
    fields = ("request_id","request_type","request_date","pickup_date","request_status")
    context_object_name = 'view_request'

#Not working 404
class updateProfile(UpdateView):
    fields = ("first_name", "last_name", "email_id", "password", "address_line1", "address_line2", "city", "pincode", "contact_number")
    template_name = 'createUser.html'
    model = Account
    success_url = reverse_lazy('customer:Customer_Hub')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Account, customer_id = id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
# Issue Model to be created?
# class createIssue(CreateView):
#     model = RequestDetail
#     template_name = 'view_requests.html'
#     fields = ("request_id","request_type","request_date","pickup_date","request_status")
#     context_object_name = 'view_request'

# class updateRoute(UpdateView):
#     fields = ("route_id","route_name",)
#     template_name = 'create.html'
#     model = Route
#     success_url = reverse_lazy('admintask:list_route')

#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Route, route_id = id_)

#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Route, route_id = id_)
