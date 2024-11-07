from django.urls import path
from .views import (
    ListaAtasView, DetalhesAtaView, AdicionarAtaView, EditarAtaView, DeletarAtaView,
    ListaPautasView, DetalhesPautaView, AdicionarPautaView, EditarPautaView, DeletarPautaView
)

app_name = 'atas'

urlpatterns = [
    # URLs para Ata
    path('atas/', ListaAtasView.as_view(), name='lista_atas'),
    path('atas/adicionar/', AdicionarAtaView.as_view(), name='adicionar_ata'),
    path('atas/<int:pk>/', DetalhesAtaView.as_view(), name='detalhes_ata'),
    path('atas/editar/<int:pk>/', EditarAtaView.as_view(), name='editar_ata'),
    path('atas/deletar/<int:pk>/', DeletarAtaView.as_view(), name='deletar_ata'),

    # URLs para Pauta
    path('pautas/', ListaPautasView.as_view(), name='lista_pautas'),
    path('pautas/adicionar/', AdicionarPautaView.as_view(), name='adicionar_pauta'),
    path('pautas/<int:pk>/', DetalhesPautaView.as_view(), name='detalhes_pauta'),
    path('pautas/editar/<int:pk>/', EditarPautaView.as_view(), name='editar_pauta'),
    path('pautas/deletar/<int:pk>/', DeletarPautaView.as_view(), name='deletar_pauta'),
]
