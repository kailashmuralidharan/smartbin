from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)
from mgr_database.models import Trip, RequestDetail, Customer, Account, Issues_Detail
from .forms import IssueForm
from mgr_truckdriver.driverindex import TruckDriverIndex
from django.utils import timezone

class ScheduledTripListView(ListView):
    context_object_name = 'sch_trip_lst'
    model = Trip
    template_name = 'scheduled_trips.html'

    def get_queryset(self):
        scheduledTripObjects = Trip.objects.filter(truck_driver_id=99).filter(trip_status = 'PROGRESS') | Trip.objects.filter(truck_driver_id=99).filter(trip_status = 'SCHEDULED') 
        return scheduledTripObjects

class CompletedTripListView(ListView):
    context_object_name = 'comp_trip_lst'
    model = Trip
    template_name = 'completed_trips.html'

    def get_queryset(self):
        completedTripObjects = Trip.objects.filter(truck_driver_id=99).filter(trip_status = 'COMPLETED')
        return completedTripObjects

class IssuesListView(ListView):
    context_object_name = 'issue_lst'
    model = Issues_Detail
    template_name = 'issue_list.html'

    def get_queryset(self):
        issueObjects = Issues_Detail.objects.filter(reported_by=99)
        return issueObjects



def start_trip(request,pk):
    if request.method == "POST":
        trip_obj = get_object_or_404(Trip,pk=pk)
        trip_obj.trip_status = "PROGRESS"
        trip_obj.save()
    
    scheduled_list = RequestDetail.objects.filter(trip_id=pk).filter(request_status="Scheduled").filter(pickup_date=timezone.now())
    completed_list = RequestDetail.objects.filter(trip_id=pk).filter(request_status="Completed").filter(pickup_date=timezone.now())
    truckdriver_dict = {
        'scheduled_requests' : scheduled_list,
        'completed_requests' : completed_list,
    }
    return render(request, 'request_list.html', truckdriver_dict)
    #return redirect('truckdriver:request_list')

#def request_list(request,pk):
    
def view_trip(request,pk): 
    
    scheduled_list = RequestDetail.objects.filter(trip_id=pk).filter(request_status="Scheduled").filter(pickup_date=timezone.now())
    completed_list = RequestDetail.objects.filter(trip_id=pk).filter(request_status="Completed").filter(pickup_date=timezone.now())
    truckdriver_dict = {
        'scheduled_requests' : scheduled_list,
        'completed_requests' : completed_list,
    }
    return render(request, 'request_list.html', truckdriver_dict)

def bin_location(request,pk):
    bin_obj = get_object_or_404(RequestDetail, pk=pk)
    cust_obj = get_object_or_404(Customer,pk=bin_obj.customer_id)
    account_obj = get_object_or_404(Account,pk=cust_obj.user_id)
    bin_obj.bin_location = account_obj.address_line1+", "+account_obj.address_line2+", "+account_obj.city+", "+account_obj.pincode
    bin_obj.bin_weight = cust_obj.general_bin_qty + cust_obj.recycle_bin_qty  + cust_obj.compost_bin_qty 
    return render(request, 'bin_location.html', {'bin_obj': bin_obj})


#change this later:

def complete_request(request,request_pk,trip_pk):
    if request.method == "POST":
        print("reached here")
        request_obj = get_object_or_404(RequestDetail,pk=request_pk)
        request_obj.request_status = "COMPLETED"
        request_obj.save()
    #return redirect('truckdriver:view_trip')

def report_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST)
        if form.is_valid():
            issue_obj = form.save(commit=False)
            issue_obj.reported_date = timezone.now()
            issue_obj.reported_by = "99"
            issue_obj.save()
            return redirect('truckdriver:issue_detail', pk=issue_obj.pk)
    else:
        form = IssueForm()
    
    
    issue_dict = {
        'form': form,
        }
    
    return render(request, 'issue_edit.html', issue_dict)

def issue_detail(request, pk):
    issue_obj = get_object_or_404(Issues_Detail, pk=pk)
    return render(request, 'issue_detail.html', {'issue_obj': issue_obj})

def issue_edit(request, pk):
    issue_obj = get_object_or_404(Issues_Detail, pk=pk)
    if request.method == "POST":
        form = IssueForm(request.POST, instance=issue_obj)
        if form.is_valid():
            issue_obj = form.save(commit=False)
            issue_obj.reported_date = timezone.now()
            issue_obj.reported_by = "99"
            issue_obj.save()
            return redirect('truckdriver:issue_detail', pk=issue_obj.pk)
    else:
        form = IssueForm(instance=issue_obj)
        
    issue_dict = {
        'form': form,
        'issue_obj': issue_obj,
        }

    return render(request, 'issue_edit.html', issue_dict)       

