# financeiro/urls.py

from django.urls import path
from .views import (
    ListaReceitasView, AdicionarReceitaView, EditarReceitaView, DeletarReceitaView,
    ListaDespesasView, AdicionarDespesaView, EditarDespesaView, DeletarDespesaView,
    ListaFolhasPagamentoView, DetalhesFolhaPagamentoView, AdicionarFolhaPagamentoView, EditarFolhaPagamentoView, DeletarFolhaPagamentoView,
    ListaLicitacoesView, DetalhesLicitacaoView, AdicionarLicitacaoView, EditarLicitacaoView, DeletarLicitacaoView,
    ListaContratosView, DetalhesContratoView, AdicionarContratoView, EditarContratoView, DeletarContratoView,
    ListaPrestacoesContasView, DetalhesPrestacaoContasView, AdicionarPrestacaoContasView, EditarPrestacaoContasView, DeletarPrestacaoContasView,
    ListaFontesReceitaView, AdicionarFonteReceitaView, EditarFonteReceitaView, DeletarFonteReceitaView,
    ListaCategoriasDespesaView, AdicionarCategoriaDespesaView, EditarCategoriaDespesaView, DeletarCategoriaDespesaView,
    DashboardFinanceiroView
)

app_name = 'financeiro'

urlpatterns = [
    path('', DashboardFinanceiroView.as_view(), name='dashboard_financeiro'),
    # URLs para Receitas
    path('receitas/', ListaReceitasView.as_view(), name='lista_receitas'),
    path('receitas/adicionar/', AdicionarReceitaView.as_view(), name='adicionar_receita'),
    path('receitas/editar/<int:pk>/', EditarReceitaView.as_view(), name='editar_receita'),
    path('receitas/deletar/<int:pk>/', DeletarReceitaView.as_view(), name='deletar_receita'),

    # URLs para Despesas
    path('despesas/', ListaDespesasView.as_view(), name='lista_despesas'),
    path('despesas/adicionar/', AdicionarDespesaView.as_view(), name='adicionar_despesa'),
    path('despesas/editar/<int:pk>/', EditarDespesaView.as_view(), name='editar_despesa'),
    path('despesas/deletar/<int:pk>/', DeletarDespesaView.as_view(), name='deletar_despesa'),

    # URLs para Folhas de Pagamento
    path('folhas_pagamento/', ListaFolhasPagamentoView.as_view(), name='lista_folhas_pagamento'),
    path('folhas_pagamento/<int:pk>/', DetalhesFolhaPagamentoView.as_view(), name='detalhar_folha_pagamento'),
    path('folhas_pagamento/adicionar/', AdicionarFolhaPagamentoView.as_view(), name='adicionar_folha_pagamento'),
    path('folhas_pagamento/editar/<int:pk>/', EditarFolhaPagamentoView.as_view(), name='editar_folha_pagamento'),
    path('folhas_pagamento/deletar/<int:pk>/', DeletarFolhaPagamentoView.as_view(), name='deletar_folha_pagamento'),

    # URLs para Licitações
    path('licitacoes/', ListaLicitacoesView.as_view(), name='lista_licitacoes'),
    path('licitacoes/<int:pk>/', DetalhesLicitacaoView.as_view(), name='detalhar_licitacao'),
    path('licitacoes/adicionar/', AdicionarLicitacaoView.as_view(), name='adicionar_licitacao'),
    path('licitacoes/editar/<int:pk>/', EditarLicitacaoView.as_view(), name='editar_licitacao'),
    path('licitacoes/deletar/<int:pk>/', DeletarLicitacaoView.as_view(), name='deletar_licitacao'),

    # URLs para Contratos
    path('contratos/', ListaContratosView.as_view(), name='lista_contratos'),
    path('contratos/<int:pk>/', DetalhesContratoView.as_view(), name='detalhar_contrato'),
    path('contratos/adicionar/', AdicionarContratoView.as_view(), name='adicionar_contrato'),
    path('contratos/editar/<int:pk>/', EditarContratoView.as_view(), name='editar_contrato'),
    path('contratos/deletar/<int:pk>/', DeletarContratoView.as_view(), name='deletar_contrato'),

    # URLs para Prestações de Contas
    path('prestacoes_contas/', ListaPrestacoesContasView.as_view(), name='lista_prestacoes_contas'),
    path('prestacoes_contas/<int:pk>/', DetalhesPrestacaoContasView.as_view(), name='detalhar_prestacao_contas'),
    path('prestacoes_contas/adicionar/', AdicionarPrestacaoContasView.as_view(), name='adicionar_prestacao_contas'),
    path('prestacoes_contas/editar/<int:pk>/', EditarPrestacaoContasView.as_view(), name='editar_prestacao_contas'),
    path('prestacoes_contas/deletar/<int:pk>/', DeletarPrestacaoContasView.as_view(), name='deletar_prestacao_contas'),

    # URLs para Fontes de Receita
    path('fontes_receita/', ListaFontesReceitaView.as_view(), name='lista_fontes_receita'),
    path('fontes_receita/adicionar/', AdicionarFonteReceitaView.as_view(), name='adicionar_fonte_receita'),
    path('fontes_receita/editar/<int:pk>/', EditarFonteReceitaView.as_view(), name='editar_fonte_receita'),
    path('fontes_receita/deletar/<int:pk>/', DeletarFonteReceitaView.as_view(), name='deletar_fonte_receita'),

    # URLs para Categorias de Despesa
    path('categorias_despesa/', ListaCategoriasDespesaView.as_view(), name='lista_categorias_despesa'),
    path('categorias_despesa/adicionar/', AdicionarCategoriaDespesaView.as_view(), name='adicionar_categoria_despesa'),
    path('categorias_despesa/editar/<int:pk>/', EditarCategoriaDespesaView.as_view(), name='editar_categoria_despesa'),
    path('categorias_despesa/deletar/<int:pk>/', DeletarCategoriaDespesaView.as_view(), name='deletar_categoria_despesa'),
]
