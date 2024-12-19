from django.urls import path
from . import views

app_name = "manage"

urlpatterns = [
    path('connexion', views.login_user, name = 'login'),
    path('deconnexion', views.logout_user, name = 'logout')
]