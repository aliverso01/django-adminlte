from django.shortcuts import render, get_object_or_404, redirect
from .models import Proposta
from .forms import PropostaForm
from django.contrib.auth.decorators import login_required

@login_required
def lista_propostas(request):
    propostas = Proposta.objects.all()
    return render(request, 'propostas/lista_propostas.html', {'propostas': propostas})

@login_required
def nova_proposta(request):
    if request.method == "POST":
        form = PropostaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_propostas')
    else:
        form = PropostaForm()
    return render(request, 'propostas/nova_proposta.html', {'form': form})

@login_required
def edita_proposta(request, pk):
    proposta = get_object_or_404(Proposta, pk=pk)
    if request.method == "POST":
        form = PropostaForm(request.POST, instance=proposta)
        if form.is_valid():
            form.save()
            return redirect('lista_propostas')
    else:
        form = PropostaForm(instance=proposta)
    return render(request, 'propostas/edita_proposta.html', {'form': form})

@login_required
def deleta_proposta(request, pk):
    proposta = get_object_or_404(Proposta, pk=pk)
    if request.method == "POST":
        proposta.delete()
        return redirect('lista_propostas')
    return render(request, 'propostas/deleta_proposta.html', {'proposta': proposta})

@login_required
def visualiza_proposta(request, pk):
    proposta = get_object_or_404(Proposta, pk=pk)
    return render(request, 'propostas/visualiza_proposta.html', {'proposta': proposta})

@login_required
def imprime_proposta(request, pk):
    proposta = get_object_or_404(Proposta, pk=pk)
    return render(request, 'propostas/imprime_proposta.html', {'proposta': proposta})