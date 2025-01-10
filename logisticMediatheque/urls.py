from django.urls import path
from logisticMediatheque.views import views_medias, views_jeux, views_membres, views_loan

app_name = "logisticMediatheque"

urlpatterns = [
    path('', views_medias.listMedias, name = 'listMedias'),

    # urls for loans
    path('emprunt', views_loan.addLoan, name = 'addLoan'),
    path('supprimer-emprunt/<int:item_id>/<int:membre_id>', views_loan.removeLoan, name = 'removeLoan'),
    # urls for create
    path('nouveau/membre', views_membres.addMembre, name = 'addMembre'),
    path('nouveau/jeu', views_jeux.addJeu, name = 'addJeu'),
    path('nouveau/<slug:media_type>', views_medias.addMedia, name = 'addMedia'),
    # urls for update
    path('modifier/membre/<int:item_id>', views_membres.updateMembre, name = 'updateMembre'),
    path('modifier/jeu/<int:item_id>', views_jeux.updateJeu, name = 'updateJeu'),
    path('modifier/<slug:media_type>/<int:item_id>', views_medias.updateMedia, name = 'updateMedia'),
    # urls for delete
    path('supprimer-membre/<int:item_id>', views_membres.removeMembre, name = 'removeMembre'),
    path('supprimer-jeu/<int:item_id>', views_jeux.removeJeu, name = 'removeJeu'),
    path('supprimer-media/<int:item_id>', views_medias.removeMedia, name = 'removeMedia'),
    # urls for read
    path('membres', views_membres.listMembres, name = 'listMembres'),
    path('membre/<int:membre_id>', views_membres.membreDetail, name = 'membreDetail'),
    path('jeu', views_jeux.listJeux, name = 'listJeux'),
    path('jeu/<int:jeu_id>', views_jeux.jeuDetail, name = 'jeuDetail'),
    path('<slug:item_type>', views_medias.listMediasByType, name = 'listMediasByType'),
    path('<slug:item_type>/<int:item_id>', views_medias.mediaDetail, name = 'mediaDetail')
]