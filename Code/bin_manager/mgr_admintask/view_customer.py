from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, FormView, DeleteView)
from django.urls import reverse_lazy, reverse
from .models import AccountForm, CustomerBinForm

from mgr_database.models import  Account, Customer


class createCustomer(CreateView):
    template_name = 'create.html'
    form_class = AccountForm
    success_url = reverse_lazy('admintask:create_bin')

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class createBinBlockRelation(CreateView):
    template_name = 'create.html'
    form_class = CustomerBinForm
    success_url = '/admin/success/'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
        
# class listBlock(ListView):
#     model = Block
#     template_name = 'list_block.html'
#     context_object_name = 'list_block'
#
# class updateBlock(UpdateView):
#     fields = ("block_name","route",)
#     template_name = 'create.html'
#     model = Block
#     success_url = reverse_lazy('admintask:list_block')
#     # success_url = reverse_lazy('admintask:list_route')
#
#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Block, block_id = id_)
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super().form_valid(form)
#
# class deleteBlock(DeleteView):
#     model = Block
#     success_url = reverse_lazy('admintask:list_block')
#
#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(Block, block_id = id_)
