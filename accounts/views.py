from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from users.forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth import login, logout
from users.models import CustomUser
from .forms import UserForm

def signup_view (request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('accounts:profile', user_id=user.id)
    else: 
      return render(request, 'accounts/signup.html', { 'form': form })
  else:
    form = UserRegistrationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view (request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)
      return redirect('accounts:profile', user_id=user.id)
    else:
      return render(request, 'accounts/login.html', {'form': form})
  else:
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def profile_view (request, user_id):
  if request.user.id == user_id:
    form = UserForm(instance=request.user)
    if request.method == 'POST':
      form = UserForm(request.POST, request.FILES, instance=request.user)
      if form.is_valid:
        form.save()
      else: 
        print(form)
    return render(request, 'accounts/profile.html', { 'requested_user': request.user, 'is_current_user': True, 'form': form })
  else:
    requested_user = CustomUser.objects.get(pk=user_id)
    return render(request, 'accounts/profile.html', {'requested_user': requested_user  })

def logout_view(request):
  if request.method == 'POST':
    logout(request)
    return redirect('accounts:login')