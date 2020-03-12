from django import forms
from .models import *

class UserForm(forms.ModelForm):
    name = forms.CharField(widget = forms.TextInput(), required = True, max_length = 20)
    phone = forms.CharField(widget = forms.TextInput(), required = True, max_length = 20)
    email = forms.EmailField(required = True)
    password = forms.CharField(widget = forms.PasswordInput(), required = True, max_length = 20)
    re_password = forms.CharField(widget = forms.PasswordInput(), required = True, max_length = 20)
    role = forms.CharField(widget = forms.TextInput(), required = True, max_length = 20)
    class Meta():
        model = AppUser
        fields = ['name', 'phone', 'email', 'password', 'role']