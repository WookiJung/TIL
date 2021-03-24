from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm, CustomPasswordChangeForm
from .models import User
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()

def main(request):
    return render(request, 'base.html')

def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user,
        }
    return render(request, 'accounts/profile.html', context)

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:profile', username=user.username)
    else:
        form = CustomUserCreationForm()
    context = {'form' : form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:profile', username=form.get_user().username)
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:main')

@login_required
def update(request, username):
    user = get_object_or_404(User, username=request.user.username)
    context = {'user' : user}
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance = user)
    context['form'] = form
    return render(request, 'accounts/update.html', context)
    

@login_required
@require_POST
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:main')

@login_required
def password(request):
    if request.method=='POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile', form.user.username)
    else:
        form = CustomPasswordChangeForm(request.user)
    context={'form':form}
    return render(request, 'accounts/pwd.html', context)
