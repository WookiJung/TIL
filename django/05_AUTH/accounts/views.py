from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

User = get_user_model()

def index(request):
    users = User.objects.all()
    context = {'users': users, }
    return render(request, 'accounts/index.html', context)


def signup(request):
    #  login 한 사용자라면,
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form, }
    
    return render(request, 'accounts/signup.html', context)


def login(request):
    # login 검증 / HTML 만드는 forms.Form 을 써서 완료
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인을 시켜야 하는데..
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {'form': form, }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')