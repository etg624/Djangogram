from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['profile_pic', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)
