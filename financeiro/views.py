from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from .models import Receita, Despesa, FonteReceita, CategoriaDespesa, FolhaPagamento, Licitacao, Contrato, PrestacaoContas
from .forms import ReceitaForm, DespesaForm, FolhaPagamentoForm, LicitacaoForm, ContratoForm, PrestacaoContasForm, FonteReceitaForm, CategoriaDespesaForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Views para Receita
class ListaReceitasView(LoginRequiredMixin, ListView):
    model = Receita
    template_name = 'financeiro/lista_receitas.html'
    context_object_name = 'receitas'

class AdicionarReceitaView(LoginRequiredMixin, CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'financeiro/form_receita.html'
    success_url = reverse_lazy('financeiro:lista_receitas')

class EditarReceitaView(LoginRequiredMixin, UpdateView):
    model = Receita
    form_class = ReceitaForm
    template_name = 'financeiro/form_receita.html'
    success_url = reverse_lazy('financeiro:lista_receitas')

class DeletarReceitaView(LoginRequiredMixin, DeleteView):
    model = Receita
    template_name = 'financeiro/confirmar_exclusao_receita.html'
    success_url = reverse_lazy('financeiro:lista_receitas')

# Views para Despesa
class ListaDespesasView(LoginRequiredMixin, ListView):
    model = Despesa
    template_name = 'financeiro/lista_despesas.html'
    context_object_name = 'despesas'

class AdicionarDespesaView(LoginRequiredMixin, CreateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'financeiro/form_despesa.html'
    success_url = reverse_lazy('financeiro:lista_despesas')

class EditarDespesaView(LoginRequiredMixin, UpdateView):
    model = Despesa
    form_class = DespesaForm
    template_name = 'financeiro/form_despesa.html'
    success_url = reverse_lazy('financeiro:lista_despesas')

class DeletarDespesaView(LoginRequiredMixin, DeleteView):
    model = Despesa
    template_name = 'financeiro/confirmar_exclusao_despesa.html'
    success_url = reverse_lazy('financeiro:lista_despesas')

# Views para Folha de Pagamento
class ListaFolhasPagamentoView(LoginRequiredMixin, ListView):
    model = FolhaPagamento
    template_name = 'financeiro/lista_folhas_pagamento.html'
    context_object_name = 'folhas_pagamento'

class DetalhesFolhaPagamentoView(LoginRequiredMixin, DetailView):
    model = FolhaPagamento
    template_name = 'financeiro/detalhes_folha_pagamento.html'
    context_object_name = 'folha'

class AdicionarFolhaPagamentoView(LoginRequiredMixin, CreateView):
    model = FolhaPagamento
    form_class = FolhaPagamentoForm
    template_name = 'financeiro/form_folha_pagamento.html'
    success_url = reverse_lazy('financeiro:lista_folhas_pagamento')

class EditarFolhaPagamentoView(LoginRequiredMixin, UpdateView):
    model = FolhaPagamento
    form_class = FolhaPagamentoForm
    template_name = 'financeiro/form_folha_pagamento.html'
    success_url = reverse_lazy('financeiro:lista_folhas_pagamento')

class DeletarFolhaPagamentoView(LoginRequiredMixin, DeleteView):
    model = FolhaPagamento
    template_name = 'financeiro/confirmar_exclusao_folha_pagamento.html'
    success_url = reverse_lazy('financeiro:lista_folhas_pagamento')

# Views para Licitação
class ListaLicitacoesView(LoginRequiredMixin, ListView):
    model = Licitacao
    template_name = 'financeiro/lista_licitacoes.html'
    context_object_name = 'licitacoes'

class DetalhesLicitacaoView(LoginRequiredMixin, DetailView):
    model = Licitacao
    template_name = 'financeiro/detalhes_licitacao.html'
    context_object_name = 'licitacao'

class AdicionarLicitacaoView(LoginRequiredMixin, CreateView):
    model = Licitacao
    form_class = LicitacaoForm
    template_name = 'financeiro/form_licitacao.html'
    success_url = reverse_lazy('financeiro:lista_licitacoes')

class EditarLicitacaoView(LoginRequiredMixin, UpdateView):
    model = Licitacao
    form_class = LicitacaoForm
    template_name = 'financeiro/form_licitacao.html'
    success_url = reverse_lazy('financeiro:lista_licitacoes')

class DeletarLicitacaoView(LoginRequiredMixin, DeleteView):
    model = Licitacao
    template_name = 'financeiro/confirmar_exclusao_licitacao.html'
    success_url = reverse_lazy('financeiro:lista_licitacoes')

# Views para Contrato
class ListaContratosView(LoginRequiredMixin, ListView):
    model = Contrato
    template_name = 'financeiro/lista_contratos.html'
    context_object_name = 'contratos'

class DetalhesContratoView(LoginRequiredMixin, DetailView):
    model = Contrato
    template_name = 'financeiro/detalhes_contrato.html'
    context_object_name = 'contrato'

class AdicionarContratoView(LoginRequiredMixin, CreateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'financeiro/form_contrato.html'
    success_url = reverse_lazy('financeiro:lista_contratos')

class EditarContratoView(LoginRequiredMixin, UpdateView):
    model = Contrato
    form_class = ContratoForm
    template_name = 'financeiro/form_contrato.html'
    success_url = reverse_lazy('financeiro:lista_contratos')

class DeletarContratoView(LoginRequiredMixin, DeleteView):
    model = Contrato
    template_name = 'financeiro/confirmar_exclusao_contrato.html'
    success_url = reverse_lazy('financeiro:lista_contratos')

# Views para Prestação de Contas
class ListaPrestacoesContasView(LoginRequiredMixin, ListView):
    model = PrestacaoContas
    template_name = 'financeiro/lista_prestacoes_contas.html'
    context_object_name = 'prestacoes_contas'

class DetalhesPrestacaoContasView(LoginRequiredMixin, DetailView):
    model = PrestacaoContas
    template_name = 'financeiro/detalhes_prestacao_contas.html'
    context_object_name = 'prestacao_contas'

class AdicionarPrestacaoContasView(LoginRequiredMixin, CreateView):
    model = PrestacaoContas
    form_class = PrestacaoContasForm
    template_name = 'financeiro/form_prestacao_contas.html'
    success_url = reverse_lazy('financeiro:lista_prestacoes_contas')

class EditarPrestacaoContasView(LoginRequiredMixin, UpdateView):
    model = PrestacaoContas
    form_class = PrestacaoContasForm
    template_name = 'financeiro/form_prestacao_contas.html'
    success_url = reverse_lazy('financeiro:lista_prestacoes_contas')

class DeletarPrestacaoContasView(LoginRequiredMixin, DeleteView):
    model = PrestacaoContas
    template_name = 'financeiro/confirmar_exclusao_prestacao_contas.html'
    success_url = reverse_lazy('financeiro:lista_prestacoes_contas')

# Views para FonteReceita
class ListaFontesReceitaView(LoginRequiredMixin, ListView):
    model = FonteReceita
    template_name = 'financeiro/lista_fontes_receita.html'
    context_object_name = 'fontes_receita'

class AdicionarFonteReceitaView(LoginRequiredMixin, CreateView):
    model = FonteReceita
    form_class = FonteReceitaForm
    template_name = 'financeiro/form_fonte_receita.html'
    success_url = reverse_lazy('financeiro:lista_fontes_receita')

class EditarFonteReceitaView(LoginRequiredMixin, UpdateView):
    model = FonteReceita
    form_class = FonteReceitaForm
    template_name = 'financeiro/form_fonte_receita.html'
    success_url = reverse_lazy('financeiro:lista_fontes_receita')

class DeletarFonteReceitaView(LoginRequiredMixin, DeleteView):
    model = FonteReceita
    template_name = 'financeiro/confirmar_exclusao_fonte_receita.html'
    success_url = reverse_lazy('financeiro:lista_fontes_receita')

# Views para CategoriaDespesa
class ListaCategoriasDespesaView(LoginRequiredMixin, ListView):
    model = CategoriaDespesa
    template_name = 'financeiro/lista_categorias_despesa.html'
    context_object_name = 'categorias_despesa'

class AdicionarCategoriaDespesaView(LoginRequiredMixin, CreateView):
    model = CategoriaDespesa
    form_class = CategoriaDespesaForm
    template_name = 'financeiro/form_categoria_despesa.html'
    success_url = reverse_lazy('financeiro:lista_categorias_despesa')

class EditarCategoriaDespesaView(LoginRequiredMixin, UpdateView):
    model = CategoriaDespesa
    form_class = CategoriaDespesaForm
    template_name = 'financeiro/form_categoria_despesa.html'
    success_url = reverse_lazy('financeiro:lista_categorias_despesa')

class DeletarCategoriaDespesaView(LoginRequiredMixin, DeleteView):
    model = CategoriaDespesa
    template_name = 'financeiro/confirmar_exclusao_categoria_despesa.html'
    success_url = reverse_lazy('financeiro:lista_categorias_despesa')

# Dashboard
class DashboardFinanceiroView(LoginRequiredMixin, View):
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
