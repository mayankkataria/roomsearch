from django import forms
from .models import *
from django.contrib.auth import authenticate, login, logout, get_user_model

class UserForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('Manager', 'Manager'),
        ('Customer', 'Customer')
    ]
    name = forms.CharField(widget = forms.TextInput(), max_length = 20, required = True) # by default required field is true
    phone = forms.CharField(widget = forms.TextInput(), max_length = 20, required = True)
    email = forms.EmailField(required = True)
    password = forms.CharField(widget = forms.PasswordInput(), max_length = 20, required = True)
    re_password = forms.CharField(widget = forms.PasswordInput(), max_length = 20, required = True)
    # role = forms.ChoiceField(widget=forms.CheckboxSelectMultiple, choices=[('manager', 'Manager'), ('customer', 'Customer')], required = False)
    role = forms.CharField(widget=forms.Select(choices=ROLE_CHOICES), max_length=20)
    class Meta():
        model = AppUser
        fields = ['name', 'phone', 'email', 'password', 'role']
        
class LoginForm(forms.Form):
    email = forms.EmailField(required = True)
    password = forms.CharField(widget=forms.PasswordInput, required = True)
