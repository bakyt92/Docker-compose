from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Перенаправление на главную страницу
    else:
        form = SignUpForm()
    return render(request, 'auth_test/signup.html', {'form': form})


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Укажите здесь ваш URL перенаправления
    else:
        form = LoginForm()
    return render(request, 'auth_test/login.html', {'form': form})