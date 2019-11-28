from django import forms
from mgr_database.models import Issues_Detail

class IssueForm(forms.ModelForm):

    class Meta:
        model = Issues_Detail
        fields = ('issue_type', 'issue_desc',)
