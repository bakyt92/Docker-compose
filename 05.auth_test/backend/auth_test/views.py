from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


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