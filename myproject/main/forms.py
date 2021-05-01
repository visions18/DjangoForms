from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    contact = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)