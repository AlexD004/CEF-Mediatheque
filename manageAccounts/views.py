from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from logisticMediatheque.views import Medias
from django.shortcuts import render


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            items = Medias.objects.all()
            return render(request, 'logisticMediatheque/lists/listMedias.html',{'items': items})
        else:
            messages.info(request, "Identifiant ou mot de passe incorrect")
    
    form = AuthenticationForm()
    return render(request, 'manageAccounts/login.html',{'form': form})


def logout_user(request):
    logout(request)
    items = Medias.objects.all()
    return render(request, 'logisticMediatheque/lists/listMedias.html',{'items': items})