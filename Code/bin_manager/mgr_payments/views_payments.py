from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView,DetailView)
from django.urls import reverse_lazy, reverse

from mgr_payments import billGenerator

# Create your views here.

class listGeneratedBills(ListView):
    model = billGenerator.customerBillDetail
    template_name = 'payment_list_BillDetails.html'
    customerBillGenerator = billGenerator.CustomerBillGenerator()
    customerBillGenerator.GenerateBill()
    queryset= customerBillGenerator.customerBillDetails

    context_object_name = 'list_BillDetails'
