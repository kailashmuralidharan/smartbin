from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)
from mgr_database.models import RequestDetail
from mgr_admintask.adminindex import AdminIndex
from mgr_database.models import  Route, Account, RequestDetail, Block, TruckDriver, Truck
from django.http import HttpResponse
from mgr_admintask.forms import TripForm
from django.urls import reverse_lazy, reverse
from .view_route import createRoute, updateRoute, deleteRoute, listRoute
from .view_block import createBlock, updateBlock, deleteBlock, listBlock
# from mgr_admintask.admincreate import createTrip
# Create your views here.

# class AdminIndex(TemplateView):
#     template_name = 'base_admin.html'


class successView(TemplateView):
    template_name = 'success.html'

class createCustomer(FormView):
    pass


class createRequest(CreateView):
    template_name = 'create.html'
    model = RequestDetail
    success_url = '/admin/success/'
    fields = '__all__'

# class createBlock(CreateView):
#     template_name = 'create.html'
#     form_class = BlockForm
#     success_url = '/admin/success/'
#
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         return super().form_valid(form)

class createTruck(CreateView):
    template_name = 'create.html'
    model = Truck
    success_url = '/admin/success/'
    fields = '__all__'

class createTruckDriver(CreateView):
    template_name = 'create.html'
    model = TruckDriver
    success_url = '/admin/success/'
    fields = '__all__'

# class createCustomer(CreateView):
#     template_name = 'create_trip.html'
#     model = Account
#     success_url = '/admin/success/'
#     fields = ['user_id','first_name','last_name','email_id','password','address_line1','address_line2','city', 'pincode', 'contact_number', 'user_type_id'
#     ]
#
#     # fields = '__all__'
#     initial = {
#     'user_type_id' : 1
#     }



class RequestListView(ListView):
    context_object_name = 'req_lst'
    model = RequestDetail
    template_name = 'demand.html'

    def get_queryset(self):
        return RequestDetail.objects.filter(pickup_date = '2019-11-20')


class CreateTripView(FormView):
    template_name = 'create.html'
    form_class = TripForm
    success_url = '/admin/success/'

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)
