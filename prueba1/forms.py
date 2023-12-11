from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'apellido', 'documento', 'direccion', 'celular', 'email', 'password1', 'password2')