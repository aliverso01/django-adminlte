from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import Receita, Despesa, FonteReceita, CategoriaDespesa, FolhaPagamento, Licitacao, Contrato, PrestacaoContas
from .forms import ReceitaForm, DespesaForm, FolhaPagamentoForm, LicitacaoForm, ContratoForm, PrestacaoContasForm, FonteReceitaForm, CategoriaDespesaForm

# Views para Receita
class ListaReceitasView(ListView):
    model = Receita
    template_name = 'financeiro/lista_receitas.html'
    context_object_name = 'receitas'

class AdicionarReceitaView(CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'financeiro/form_receita.html'
    success_url = reverse_lazy('financeiro:lista_receitas')

class EditarReceitaView(UpdateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'financeiro/form_receita.html'
    success_url = reverse_lazy('financeiro:lista_receitas')

class DeletarReceitaView(DeleteView):
    model = Receita
    template_name = 'financeiro/confirmar_exclusao_receita.html'
    success_url = reverse_lazy('financeiro:lista_receitas')

# Views para Despesa
class ListaDespesasView(ListView):
    model = Despesa
    template_name = 'financeiro/lista_despesas.html'
    context_object_name = 'despesas'

class AdicionarDespesaView(CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'financeiro/form_despesa.html'
    success_url = reverse_lazy('financeiro:lista_despesas')

class EditarDespesaView(UpdateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'financeiro/form_despesa.html'
    success_url = reverse_lazy('financeiro:lista_despesas')

class DeletarDespesaView(DeleteView):
    model = Despesa
    template_name = 'financeiro/confirmar_exclusao_despesa.html'
    success_url = reverse_lazy('financeiro:lista_despesas')

# Views para Folha de Pagamento
class ListaFolhasPagamentoView(ListView):
    model = FolhaPagamento
    template_name = 'financeiro/lista_folhas_pagamento.html'
    context_object_name = 'folhas_pagamento'

class DetalhesFolhaPagamentoView(DetailView):
    model = FolhaPagamento
    template_name = 'financeiro/detalhes_folha_pagamento.html'
    context_object_name = 'folha'

class AdicionarFolhaPagamentoView(CreateView):
    model = FolhaPagamento
    form_class = FolhaPagamentoForm
    template_name = 'financeiro/form_folha_pagamento.html'
    success_url = reverse_lazy('financeiro:lista_folhas_pagamento')

class EditarFolhaPagamentoView(UpdateView):
    model = FolhaPagamento
    form_class = FolhaPagamentoForm
    template_name = 'financeiro/form_folha_pagamento.html'
    success_url = reverse_lazy('financeiro:lista_folhas_pagamento')

class DeletarFolhaPagamentoView(DeleteView):
    model = FolhaPagamento
    template_name = 'financeiro/confirmar_exclusao_folha_pagamento.html'
    success_url = reverse_lazy('financeiro:lista_folhas_pagamento')

# Views para Licitação
class ListaLicitacoesView(ListView):
    model = Licitacao
    template_name = 'financeiro/lista_licitacoes.html'
    context_object_name = 'licitacoes'

class DetalhesLicitacaoView(DetailView):
    model = Licitacao
    template_name = 'financeiro/detalhes_licitacao.html'
    context_object_name = 'licitacao'

class AdicionarLicitacaoView(CreateView):
    model = Licitacao
    form_class = LicitacaoForm
    template_name = 'financeiro/form_licitacao.html'
    success_url = reverse_lazy('financeiro:lista_licitacoes')

class EditarLicitacaoView(UpdateView):
    model = Licitacao
    form_class = LicitacaoForm
    template_name = 'financeiro/form_licitacao.html'
    success_url = reverse_lazy('financeiro:lista_licitacoes')

class DeletarLicitacaoView(DeleteView):
    model = Licitacao
    template_name = 'financeiro/confirmar_exclusao_licitacao.html'
    success_url = reverse_lazy('financeiro:lista_licitacoes')

# Views para Contrato
class ListaContratosView(ListView):
    model = Contrato
    template_name = 'financeiro/lista_contratos.html'
    context_object_name = 'contratos'

class DetalhesContratoView(DetailView):
    model = Contrato
    template_name = 'financeiro/detalhes_contrato.html'
    context_object_name = 'contrato'

class AdicionarContratoView(CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'financeiro/form_contrato.html'
    success_url = reverse_lazy('financeiro:lista_contratos')

class EditarContratoView(UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'financeiro/form_contrato.html'
    success_url = reverse_lazy('financeiro:lista_contratos')

class DeletarContratoView(DeleteView):
    model = Contrato
    template_name = 'financeiro/confirmar_exclusao_contrato.html'
    success_url = reverse_lazy('financeiro:lista_contratos')

# Views para Prestação de Contas
class ListaPrestacoesContasView(ListView):
    model = PrestacaoContas
    template_name = 'financeiro/lista_prestacoes_contas.html'
    context_object_name = 'prestacoes_contas'

class DetalhesPrestacaoContasView(DetailView):
    model = PrestacaoContas
    template_name = 'financeiro/detalhes_prestacao_contas.html'
    context_object_name = 'prestacao_contas'

class AdicionarPrestacaoContasView(CreateView):
    model = PrestacaoContas
    form_class = PrestacaoContasForm
    template_name = 'financeiro/form_prestacao_contas.html'
    success_url = reverse_lazy('financeiro:lista_prestacoes_contas')

class EditarPrestacaoContasView(UpdateView):
    model = PrestacaoContas
    form_class = PrestacaoContasForm
    template_name = 'financeiro/form_prestacao_contas.html'
    success_url = reverse_lazy('financeiro:lista_prestacoes_contas')

class DeletarPrestacaoContasView(DeleteView):
    model = PrestacaoContas
    template_name = 'financeiro/confirmar_exclusao_prestacao_contas.html'
    success_url = reverse_lazy('financeiro:lista_prestacoes_contas')

# Views para FonteReceita
class ListaFontesReceitaView(ListView):
    model = FonteReceita
    template_name = 'financeiro/lista_fontes_receita.html'
    context_object_name = 'fontes_receita'

class AdicionarFonteReceitaView(CreateView):
    model = FonteReceita
    form_class = FonteReceitaForm
    template_name = 'financeiro/form_fonte_receita.html'
    success_url = reverse_lazy('financeiro:lista_fontes_receita')

class EditarFonteReceitaView(UpdateView):
    model = FonteReceita
    form_class = FonteReceitaForm
    template_name = 'financeiro/form_fonte_receita.html'
    success_url = reverse_lazy('financeiro:lista_fontes_receita')

class DeletarFonteReceitaView(DeleteView):
    model = FonteReceita
    template_name = 'financeiro/confirmar_exclusao_fonte_receita.html'
    success_url = reverse_lazy('financeiro:lista_fontes_receita')


# Views para CategoriaDespesa
class ListaCategoriasDespesaView(ListView):
    model = CategoriaDespesa
    template_name = 'financeiro/lista_categorias_despesa.html'
    context_object_name = 'categorias_despesa'

class AdicionarCategoriaDespesaView(CreateView):
    model = CategoriaDespesa
    form_class = CategoriaDespesaForm
    template_name = 'financeiro/form_categoria_despesa.html'
    success_url = reverse_lazy('financeiro:lista_categorias_despesa')

class EditarCategoriaDespesaView(UpdateView):
    model = CategoriaDespesa
    form_class = CategoriaDespesaForm
    template_name = 'financeiro/form_categoria_despesa.html'
    success_url = reverse_lazy('financeiro:lista_categorias_despesa')

class DeletarCategoriaDespesaView(DeleteView):
    model = CategoriaDespesa
    template_name = 'financeiro/confirmar_exclusao_categoria_despesa.html'
    success_url = reverse_lazy('financeiro:lista_categorias_despesa')


#dashboard

class DashboardFinanceiroView(View):
    template_name = 'financeiro/dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {
            'receitas_count': Receita.objects.count(),
            'despesas_count': Despesa.objects.count(),
            'folhas_pagamento_count': FolhaPagamento.objects.count(),
            'licitacoes_count': Licitacao.objects.count(),
            'contratos_count': Contrato.objects.count(),
            'prestacoes_contas_count': PrestacaoContas.objects.count(),
            'fontes_receita_count': FonteReceita.objects.count(),
            'categorias_despesa_count': CategoriaDespesa.objects.count(),
        }
        return render(request, self.template_name, context)