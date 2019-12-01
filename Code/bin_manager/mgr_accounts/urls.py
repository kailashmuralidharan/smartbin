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
from django.urls import path
from mgr_accounts import views
from mgr_admintask import views as adm_v
from mgr_admintask import urls as adm_u
from django.conf.urls import include 

app_name = 'accounts'

urlpatterns = [
    # path('', views.Index.as_view(),name = 'Home'), #default
    path('', views.CustomerIndex.as_view(),name = 'Customer_Hub'),
    path('request/',views.createRequest.as_view(), name = 'request'),
    path('viewRequest/',views.viewRequests.as_view(), name = 'viewrequests'),
    path('profile/',views.updateProfile.as_view(), name = 'updateprofile'),
    path('pay/',views.payBill.as_view(), name = 'payBill'),
    # path('admin/',include(adm_u),name='admin_user')
    # path('admin/',adm_v.AdminIndex.as_view(),name='admin_user')
    # path('admin/',include('mgr_custtask.urls'),name='cust_user')
    # path('admin/',include('mgr_drivtask.urls'),name='driv_user')
]