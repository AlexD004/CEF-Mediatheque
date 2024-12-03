from django.shortcuts import render, redirect
from mediathequePython.forms.loginForm import LoginForm
from django.contrib.auth import login, logout, authenticate

def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = 'Bonjour ! Vous êtes connecté.'
            else:
                message = 'Identifiants invalides'
    return render(
        request, '../templates/login.html', context={'form': form, 'message': message})


def logout_user(request):
    logout(request)
    return redirect('login')