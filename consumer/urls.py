from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:id>/', views.detalhe, name='detalhes'),
    path('detalhes/savegame/<int:id>/', views.saveGame, name='savegame')
]