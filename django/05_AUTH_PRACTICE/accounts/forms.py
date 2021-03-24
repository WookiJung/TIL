from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class CustomPasswordChangeForm(PasswordChangeForm):
    pass
