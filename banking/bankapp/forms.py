from django import forms
from .models import Banking

class ServiceForm(forms.ModelForm):
    class Meta:
        model=Banking
        fields=['name','email','date_of_birth','address','mobile','district','branch','account_type','service_required']