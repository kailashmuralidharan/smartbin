from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)
from mgr_database.models import RequestDetail
from mgr_admintask.adminindex import AdminIndex
from mgr_database.models import  Route, Account, RequestDetail, Block, TruckDriver, Truck
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from .view_route import createRoute, updateRoute, deleteRoute, listRoute
from .view_block import createBlock, updateBlock, deleteBlock, listBlock
from .view_customer import createCustomer, createBinBlockRelation, manageCustomer, viewCustomerDetails
from .view_trips import CreateTripView
from .view_requests import createRequest
from .view_driver import createTruckDriver
from .view_truck import createTruck
# from mgr_payments import views_payments
from mgr_payments import billGenerator
from scheduler import manager


# Create your views here.


class successView(TemplateView):
    template_name = 'success.html'


class RequestListView(ListView):
    context_object_name = 'req_lst'
    model = RequestDetail
    template_name = 'demand.html'

    def get_queryset(self):
        return RequestDetail.objects.filter(pickup_date = '2019-11-20')


# class viewCustomerDetails(ListView):
#     context_object_name = 'cust_details'
#     model = Customer
#     template_name = 'display.html'
#     # queryset = Customer.objects.filter(block = 2)
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         object_list = Customer.objects.filter(
#         Q (block=query)
#         )
#         return object_list

class autoTrip(ListView):
    model = manager.Manager
    template_name = 'scheduler.html'
    context_object_name = 'scheduler_stages'

    def get_queryset(self):
        query = self.request.GET.get('autotrip')
        wasteType = ''
        if query == 'General':
            wasteType = query
            newScheduler = manager.Manager()
            newScheduler.startWork(wasteType)
            return newScheduler.stages
        elif query == 'Recycle':
            wasteType = query
            newScheduler = manager.Manager()
            newScheduler.startWork(wasteType)
            return newScheduler.stages
        elif query == 'Compost':
            wasteType = query
            newScheduler = manager.Manager()
            newScheduler.startWork(wasteType)
            return newScheduler.stages

# Create your views here.

class listGeneratedBills(ListView):
    model = billGenerator.customerBillDetail
    template_name = 'payment_list_BillDetails.html'
    context_object_name = 'list_BillDetails'

    def get_queryset(self):
        customerBillGenerator = billGenerator.CustomerBillGenerator()
        customerBillGenerator.GenerateBill()
        return customerBillGenerator.customerBillDetails

# class customerBillDetailView(DetailView):
#     model = billGenerator.customerBillDetail
#     template_name = 'payment_Customer_BillDetail.html'
#     customerBillGenerator = billGenerator.CustomerBillGenerator()
#     cache= customerBillGenerator.GetCachedResult()
#     context_object_name = 'customer_billDetailedView'
#     # def get_object(self):
#     #     id_ =self.kwargs.get("name")

#     def get_queryset(self):
#         self.customerName = get_object_or_404(billGenerator.customerBillDetail, name=self.kwargs.get("name"))
#         return self.cache.filter(name =self.customerName)
#     # def book_detail_view(self,request, name):
#     #     customer = self.cache.filter(name =self.customerName)
#     #     return render(request, 'payment_Customer_BillDetail.html', context={'customer_billDetailedView': customer})
 # path('customer_billDetailedView/<name>/', views.customerBillDetailView.as_view(),name='customer_billDetailedView'),
    # path(r'^customer_billDetailedView/(?P<name>\d+)$', views.customerBillDetailView.as_view(),name='customer_billDetailedView'),
