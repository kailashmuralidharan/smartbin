from django.db import models
from mgr_database.models import Route, Block, Account, Customer
from django.forms import ModelForm
from django import forms
from django.urls import reverse


# Create your models here.

class BlockForm(ModelForm):
    # route_id = forms.ModelChoiceField(
    # queryset=Route.objects.all()
    # )

    class Meta:
        model = Block
        fields = '__all__'


class AccountForm(ModelForm):

    email_id = forms.EmailField()
    class Meta:
        model = Account
        fields='__all__'

class CustomerBinForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerEditForm(ModelForm):
    customer_id = forms.IntegerField(disabled = True)
    user = forms.IntegerField(disabled = True)
    class Meta:
        model = Customer
        fields = '__all__'

class CustomerSearchForm(forms.Form):
    # block = forms.CharField(disabled = True )
    # user = forms.IntegerField(disabled = True)
    customer_id = forms.IntegerField()
    # user_id = forms.IntegerField()
    # class Meta:
    #     model = Customer
    #     fields = ['customer_id','user','block']
