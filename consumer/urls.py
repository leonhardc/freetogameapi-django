from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes/<int:id>/', views.detalhe, name='detalhes')
]