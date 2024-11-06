from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_propostas, name='lista_propostas'),
    path('nova/', views.nova_proposta, name='nova_proposta'),
    path('edita/<int:pk>/', views.edita_proposta, name='edita_proposta'),
    path('deleta/<int:pk>/', views.deleta_proposta, name='deleta_proposta'),
    path('visualiza/<int:pk>/', views.visualiza_proposta, name='visualiza_proposta'),
    path('imprime/<int:pk>/', views.imprime_proposta, name='imprime_proposta'),
]