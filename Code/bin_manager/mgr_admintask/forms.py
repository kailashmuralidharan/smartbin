from django.forms import ModelForm
from django import forms
from mgr_database.models import Trip


class TripForm(ModelForm):
    # trip_date = forms.DateField(widget = forms.SelectDateWidget(
    # empty_label = ("Choose Year", "Choose Month", "Choose Day"),
    # ))
    class Meta:
        model = Trip
        fields = '__all__'
