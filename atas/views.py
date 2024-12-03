from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ata, Pauta
from .forms import AtaForm, PautaForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Views para Ata
class ListaAtasView(LoginRequiredMixin, ListView):
    model = Ata
    template_name = 'atas/lista_atas.html'
    context_object_name = 'atas'

class DetalhesAtaView(LoginRequiredMixin, DetailView):
    model = Ata
    template_name = 'atas/detalhes_ata.html'
    context_object_name = 'ata'

class AdicionarAtaView(LoginRequiredMixin, CreateView):
    model = Ata
    form_class = AtaForm
    template_name = 'atas/form_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

class EditarAtaView(LoginRequiredMixin, UpdateView):
    model = Ata
    form_class = AtaForm
    template_name = 'atas/form_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

class DeletarAtaView(LoginRequiredMixin, DeleteView):
    model = Ata
    template_name = 'atas/confirmar_exclusao_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

# Views para Pauta
class ListaPautasView(LoginRequiredMixin, ListView):
    model = Pauta
    template_name = 'atas/lista_pautas.html'
    context_object_name = 'pautas'

class DetalhesPautaView(LoginRequiredMixin, DetailView):
    model = Pauta
    template_name = 'atas/detalhes_pauta.html'
    context_object_name = 'pauta'

class AdicionarPautaView(LoginRequiredMixin, CreateView):
    model = Pauta
    form_class = PautaForm
    template_name = 'atas/form_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')

class EditarPautaView(LoginRequiredMixin, UpdateView):
    model = Pauta
    form_class = PautaForm
    template_name = 'atas/form_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')

class DeletarPautaView(LoginRequiredMixin, DeleteView):
    model = Pauta
    template_name = 'atas/confirmar_exclusao_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')
