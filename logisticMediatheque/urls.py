from django.urls import path
from . import views

app_name = "logisticMediatheque"

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),

    path('emprunt', views.addLoan, name = 'addLoan'),
    path('supprimer-emprunt/<int:item_id>/<int:membre_id>', views.removeLoan, name = 'removeLoan'),

    path('nouveau/membre', views.addMembre, name = 'addMembre'),
    path('nouveau/jeu', views.addJeu, name = 'addJeu'),
    path('nouveau/<slug:media_type>', views.addMedia, name = 'addMedia'),

    path('modifier/membre/<int:item_id>', views.updateMembre, name = 'updateMembre'),
    path('modifier/jeu/<int:item_id>', views.updateJeu, name = 'updateJeu'),
    path('modifier/<slug:media_type>/<int:item_id>', views.updateMedia, name = 'updateMedia'),

    path('supprimer-membre/<int:item_id>', views.removeMembre, name = 'removeMembre'),
    path('supprimer-jeu/<int:item_id>', views.removeJeu, name = 'removeJeu'),
    path('supprimer-media/<int:item_id>', views.removeMedia, name = 'removeMedia'),

    path('membres', views.listMembres, name = 'listMembres'),
    path('membre/<int:membre_id>', views.membreDetail, name = 'membreDetail'),
    path('jeu', views.listJeux, name = 'listJeux'),
    path('jeu/<int:jeu_id>', views.jeuDetail, name = 'jeuDetail'),
    path('<slug:item_type>', views.listMedias, name = 'listMedias'),
    path('<slug:item_type>/<int:item_id>', views.mediaDetail, name = 'mediaDetail'),
    
    path('membres', views.listMembres, name = 'listMembres'),
    path('historique', views.historique, name = 'historique')
]