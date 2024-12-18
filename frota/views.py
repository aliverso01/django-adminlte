from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Veiculo, SolicitaCombustivel
from .forms import VeiculoForm, SolicitaCombustivelForm

class ListaVeiculosView(LoginRequiredMixin, ListView):
    model = Veiculo
    template_name = 'frota/lista_veiculos.html'
    context_object_name = 'veiculos'

class AdicionarVeiculoView(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'frota/form_veiculo.html'
    success_url = reverse_lazy('frota:lista_veiculos')

class EditarVeiculoView(LoginRequiredMixin, UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'frota/form_veiculo.html'
    success_url = reverse_lazy('frota:lista_veiculos')

class DeletarVeiculoView(LoginRequiredMixin, DeleteView):
    model = Veiculo
    template_name = 'frota/confirmar_exclusao_veiculo.html'
    success_url = reverse_lazy('frota:lista_veiculos')

# Listar solicitações de combustível
class ListaSolicitacoesCombustivelView(LoginRequiredMixin, ListView):
    model = SolicitaCombustivel
    template_name = 'frota/lista_solicitacoes_combustivel.html'
    context_object_name = 'solicitacoes'

# Detalhar solicitação de combustível
class DetalhesSolicitaCombustivelView(LoginRequiredMixin, DetailView):
    model = SolicitaCombustivel
    template_name = 'frota/detalhes_solicita_combustivel.html'
    context_object_name = 'solicitacao'

# Adicionar solicitação de combustível
class AdicionarSolicitaCombustivelView(LoginRequiredMixin, CreateView):
    model = SolicitaCombustivel
    form_class = SolicitaCombustivelForm
    template_name = 'frota/form_solicita_combustivel.html'
    success_url = reverse_lazy('frota:lista_solicitacoes_combustivel')

# Editar solicitação de combustível
class EditarSolicitaCombustivelView(LoginRequiredMixin, UpdateView):
    model = SolicitaCombustivel
    form_class = SolicitaCombustivelForm
    template_name = 'frota/form_solicita_combustivel.html'
    success_url = reverse_lazy('frota:lista_solicitacoes_combustivel')

# Deletar solicitação de combustível
class DeletarSolicitaCombustivelView(LoginRequiredMixin, DeleteView):
    model = SolicitaCombustivel
    template_name = 'frota/confirmar_exclusao_solicita_combustivel.html'
    success_url = reverse_lazy('frota:lista_solicitacoes_combustivel')