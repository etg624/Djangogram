from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class UserRegistrationForm(UserCreationForm):

  class Meta:
    model = CustomUser
    fields = ('username', 'profile_pic')

class CustomUserChangeForm(UserChangeForm):

  class Meta:
      model = CustomUser
      fields = ('username', 'profile_pic')
