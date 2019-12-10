from django.urls import path
from mgr_customer import views
from mgr_admintask import views as adm_v
from mgr_admintask import urls as adm_u
from django.conf.urls import include

app_name = 'customer'

urlpatterns = [
    #path('', views.index, name='index'),
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