from django.shortcuts import render

from django.views.generic import (TemplateView)
from .view_requests import createRequest, viewRequests, updateProfile
# Create your views here.


class Index(TemplateView):
    template_name = 'index.html'

# class CustomerIndex(TemplateView):
#     template_name = 'base_user.html'
#
# class payBill(TemplateView):
#     template_name = 'bill.html'
