from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    mobile = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('password2', 'first_name','last_name', 'username', 'email', 'password1', 'mobile')