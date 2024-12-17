from django.urls import path
from . import views

app_name = "logisticMediatheque"

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('livres', views.listLivres, name = 'listLivres'),
    path('cds', views.listCDs, name = 'listCDs'),
    path('dvds', views.listDVDs, name = 'listDVDs'),
    path('jeux', views.listJeux, name = 'listJeux'),
    path('livre/<int:livre_id>', views.livreDetail, name = 'livreDetail'),
    path('cd/<int:cd_id>', views.cdDetail, name = 'cdDetail'),
    path('dvd/<int:dvd_id>', views.dvdDetail, name = 'dvdDetail'),
    path('jeu/<int:jeu_id>', views.jeuDetail, name = 'jeuDetail'),
    path('membres', views.listMembres, name = 'listMembres'),
    path('historique', views.historique, name = 'historique')
]