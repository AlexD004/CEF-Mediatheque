from django.urls import path
from . import views

app_name = "logisticMediatheque"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:livre_id>', views.livreDetail, name = 'livreDetail')
]