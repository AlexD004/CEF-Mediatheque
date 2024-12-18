from django.urls import path
from . import views

app_name = "logisticMediatheque"

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('<slug:sortBy>', views.listMedias, name = 'listMedias'),
    path('<slug:item_type>/<int:item_id>', views.mediaDetail, name = 'mediaDetail'),
    path('jeu/<int:jeu_id>', views.jeuDetail, name = 'jeuDetail'),
    path('membres', views.listMembres, name = 'listMembres'),
    path('historique', views.historique, name = 'historique')
]