  
from django import forms
from django.forms.widgets import EmailInput


class SubscribeForm(forms.Form):
    email = forms.EmailField(
        widget=EmailInput(attrs={
            'placeholder': 'Email',
            'required': 'required',
            'name': 'subscribe',
        })
    )