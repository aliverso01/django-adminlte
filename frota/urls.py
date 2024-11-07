from django.urls import path
from .views import ListaVeiculosView, AdicionarVeiculoView, EditarVeiculoView, DeletarVeiculoView, ListaSolicitacoesCombustivelView, AdicionarSolicitaCombustivelView, DetalhesSolicitaCombustivelView, EditarSolicitaCombustivelView, DeletarSolicitaCombustivelView


app_name = 'frota'

urlpatterns = [
    path('', ListaVeiculosView.as_view(), name='lista_veiculos'),
    path('adicionar/', AdicionarVeiculoView.as_view(), name='adicionar_veiculo'),
    path('editar/<int:pk>/', EditarVeiculoView.as_view(), name='editar_veiculo'),
    path('deletar/<int:pk>/', DeletarVeiculoView.as_view(), name='deletar_veiculo'),

    path('solicitacoes_combustivel/', ListaSolicitacoesCombustivelView.as_view(), name='lista_solicitacoes_combustivel'),
    path('solicitacoes_combustivel/adicionar/', AdicionarSolicitaCombustivelView.as_view(), name='adicionar_solicita_combustivel'),
    path('solicitacoes_combustivel/<int:pk>/', DetalhesSolicitaCombustivelView.as_view(), name='detalhes_solicita_combustivel'),
    path('solicitacoes_combustivel/editar/<int:pk>/', EditarSolicitaCombustivelView.as_view(), name='editar_solicita_combustivel'),
    path('solicitacoes_combustivel/deletar/<int:pk>/', DeletarSolicitaCombustivelView.as_view(), name='deletar_solicita_combustivel'),
]
