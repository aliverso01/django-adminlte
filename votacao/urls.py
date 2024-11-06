from django.urls import path
from .views import lista_votacoes, nova_votacao, edita_votacao, deleta_votacao, visualiza_votacao, lista_status_votacoes, novo_status_votacao, edita_status_votacao, deleta_status_votacao, visualiza_status_votacao


urlpatterns = [
    path('', lista_votacoes, name='lista_votacoes'),
    path('nova/', nova_votacao, name='nova_votacao'),
    path('edita/<int:pk>/', edita_votacao, name='edita_votacao'),
    path('deleta/<int:pk>/', deleta_votacao, name='deleta_votacao'),
    path('visualiza/<int:pk>/', visualiza_votacao, name='visualiza_votacao'),
    path('status/', lista_status_votacoes, name='lista_status_votacoes'),
    path('status/novo/', novo_status_votacao, name='novo_status_votacao'),
    path('status/edita/<int:pk>/', edita_status_votacao, name='edita_status_votacao'),
    path('status/deleta/<int:pk>/', deleta_status_votacao, name='deleta_status_votacao'),
    path('status/visualiza/<int:pk>/', visualiza_status_votacao, name='visualiza_status_votacao'),
]