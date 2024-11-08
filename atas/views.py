from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ata, Pauta
from .forms import AtaForm, PautaForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Views para Ata
class ListaAtasView(ListView, LoginRequiredMixin):
    model = Ata
    template_name = 'atas/lista_atas.html'
    context_object_name = 'atas'

class DetalhesAtaView(DetailView):
    model = Ata
    template_name = 'atas/detalhes_ata.html'
    context_object_name = 'ata'

class AdicionarAtaView(CreateView, LoginRequiredMixin):
    model = Ata
    form_class = AtaForm
    template_name = 'atas/form_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

class EditarAtaView(UpdateView, LoginRequiredMixin):
    model = Ata
    form_class = AtaForm
    template_name = 'atas/form_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

class DeletarAtaView(DeleteView, LoginRequiredMixin):
    model = Ata
    template_name = 'atas/confirmar_exclusao_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

# Views para Pauta
class ListaPautasView(ListView, LoginRequiredMixin):
    model = Pauta
    template_name = 'atas/lista_pautas.html'
    context_object_name = 'pautas'

class DetalhesPautaView(DetailView, LoginRequiredMixin):
    model = Pauta
    template_name = 'atas/detalhes_pauta.html'
    context_object_name = 'pauta'

class AdicionarPautaView(CreateView, LoginRequiredMixin):
    model = Pauta
    form_class = PautaForm
    template_name = 'atas/form_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')

class EditarPautaView(UpdateView, LoginRequiredMixin):
    model = Pauta
    form_class = PautaForm
    template_name = 'atas/form_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')

class DeletarPautaView(DeleteView, LoginRequiredMixin):
    model = Pauta
    template_name = 'atas/confirmar_exclusao_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')
