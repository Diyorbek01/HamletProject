from django import forms
from django.forms.widgets import EmailInput, PasswordInput, TextInput

class loginForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        max_length=25,
           widget= TextInput(attrs={
            'name': 'username',
            'placeholder': 'Username',
        })
    )
    password = forms.CharField(
        widget=PasswordInput(attrs=
        {
            'name': 'password',
            'placeholder': 'Password', 
        })
    )

class registerForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        max_length=25,
        widget= TextInput(attrs={
            'name': 'username',
            'placeholder': 'Username',
            'class': 'label',
            'required': 'required'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name': 'first_name',
            'class': 'label',
            'placeholder': 'Enter name',
            'required': 'required'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        widget=TextInput(attrs={
            'name': 'last_name',
            'class': 'label',
            'placeholder': 'Enter last name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        max_length=30,
        widget=EmailInput(attrs={
            'name': 'email',
            'class': 'label',
            'placeholder': 'Enter email',
            'required': 'required'
        })
    )
    password1 = forms.CharField(
        widget=PasswordInput(attrs=
        {
            'name': 'password1',
            'placeholder': 'Password', 
            'class': 'label',
            'required': 'required'
        })
    )

    password2 = forms.CharField(
        widget=PasswordInput(attrs=
        {
            'name': 'password1',
            'placeholder': 'Password', 
            'class': 'label',
            'required': 'required'
        })
    )