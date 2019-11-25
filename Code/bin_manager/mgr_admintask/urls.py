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
from mgr_admintask import views
from django.urls import path

app_name = 'admintask'

urlpatterns = [
    path('', views.AdminIndex.as_view(),name = 'Admin_Home'),
    path('demand/',views.RequestListView.as_view(),name='demand'),
    path('success/',views.successView.as_view(),name='success_admin'),
    path('create_route/',views.createRoute.as_view(),name='create_route'),
    path('list_route/',views.listRoute.as_view(),name='list_route'),
    path('update_route/<int:id>/',views.updateRoute.as_view(),name='update_route'),
    path('delete_route/<int:id>/',views.deleteRoute.as_view(),name='delete_route'),
    path('create_block/',views.createBlock.as_view(),name='create_block'),
    path('list_block/',views.listBlock.as_view(),name='list_block'),
    path('update_block/<int:id>/',views.updateBlock.as_view(),name='update_block'),
    path('delete_block/<int:id>/',views.deleteBlock.as_view(),name='delete_block'),
    path('create_customer/',views.createCustomer.as_view(),name='create_customer'),
    path('create_bin/',views.createBinBlockRelation.as_view(),name='create_bin'),
    path('create_truck/',views.createTruck.as_view(),name='create_truck'),
    path('create_driver/',views.createTruckDriver.as_view(),name='create_driver'),
    path('create_request/',views.createRequest.as_view(),name='create_request'),
    path('create_trip/',views.CreateTripView.as_view(),name='create_trip'),
    # path('create_trip/',views.CreateTripView.as_view(),name='create_trip'),

]
