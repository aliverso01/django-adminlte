from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ata, Pauta
from .forms import AtaForm, PautaForm

# Views para Ata
class ListaAtasView(ListView):
    model = Ata
    template_name = 'atas/lista_atas.html'
    context_object_name = 'atas'

class DetalhesAtaView(DetailView):
    model = Ata
    template_name = 'atas/detalhes_ata.html'
    context_object_name = 'ata'

class AdicionarAtaView(CreateView):
    model = Ata
    form_class = AtaForm
    template_name = 'atas/form_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

class EditarAtaView(UpdateView):
    model = Ata
    form_class = AtaForm
    template_name = 'atas/form_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

class DeletarAtaView(DeleteView):
    model = Ata
    template_name = 'atas/confirmar_exclusao_ata.html'
    success_url = reverse_lazy('atas:lista_atas')

# Views para Pauta
class ListaPautasView(ListView):
    model = Pauta
    template_name = 'atas/lista_pautas.html'
    context_object_name = 'pautas'

class DetalhesPautaView(DetailView):
    model = Pauta
    template_name = 'atas/detalhes_pauta.html'
    context_object_name = 'pauta'

class AdicionarPautaView(CreateView):
    model = Pauta
    form_class = PautaForm
    template_name = 'atas/form_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')

class EditarPautaView(UpdateView):
    model = Pauta
    form_class = PautaForm
    template_name = 'atas/form_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')

class DeletarPautaView(DeleteView):
    model = Pauta
    template_name = 'atas/confirmar_exclusao_pauta.html'
    success_url = reverse_lazy('atas:lista_pautas')
