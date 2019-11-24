from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView)
from mgr_database import Account


class createTrip(CreateView):
    template_name = 'create_trip.html'
    model = Account
    fields = ['user_id','first_name','last_name','email_id','password','address_line1','address_line2','city', 'pincode', 'contact_number', 'user_type_id'
    ]


class createBlock(CreateView):
    pass

class createCustomer(CreateView):
    pass

class createRoute(CreateView):
    pass
