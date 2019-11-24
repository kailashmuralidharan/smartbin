from django.db import models
from mgr_database.models import Route, Block
from django.forms import ModelForm
from django import forms
from django.urls import reverse


# Create your models here.

# routeOptions = []
# for rt in Route.objects.all():
#     routeOptions.append(int(rt.route_id))

class BlockForm(ModelForm):
    # route_id = forms.ModelChoiceField(
    # queryset=Route.objects.all()
    # )

    class Meta:
        model = Block
        fields = '__all__'
