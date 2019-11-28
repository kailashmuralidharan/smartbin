"""bin_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from mgr_truckdriver import views
from django.urls import path

app_name = 'truckdriver'

urlpatterns = [
    path('', views.TruckDriverIndex.as_view(), name = 'TruckDriver_Home'),
    path('scheduled_trips/', views.ScheduledTripListView.as_view(), name='scheduled_trips'),
    path('completed_trips/', views.CompletedTripListView.as_view(), name='completed_trips'),
    path('trip/<int:pk>/', views.start_trip, name='start_trip'),
    path('viewtrip/<int:pk>/', views.view_trip, name='view_trip'),
    path('bin/<int:pk>/',views.bin_location, name='bin_location'),
    path('request/<int:pk>/', views.complete_request, name='complete_request'),
    path('view_issues/', views.IssuesListView.as_view(), name='view_issues'),
    path('issue/new/', views.report_issue,name='report_issue'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('issue/<int:pk>/edit/', views.issue_edit, name='issue_edit'),
]
