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
from .view_customer import createCustomer, createBinBlockRelation, manageCustomer, viewCustomerDetails
# from mgr_payments import views_payments
from mgr_payments import billGenerator


# Create your views here.


class successView(TemplateView):
    template_name = 'success.html'

# class createCustomer(FormView):
#     pass


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
