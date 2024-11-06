from django.shortcuts import render
from .models import Votacao, StatusVotacao
from .forms import VotacaoForm, StatusVotacaoForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.


def lista_votacoes(request):
    votacoes = Votacao.objects.all()
    return render(request, 'votacao/lista_votacoes.html', {'votacoes': votacoes})

def nova_votacao(request):
    if request.method == "POST":
        form = VotacaoForm(request.POST)
        if form.is_valid():
            votacao = form.save(commit=False)
            votacao.save()
            return redirect('lista_votacoes')
    else:
        form = VotacaoForm()
    return render(request, 'votacao/nova_votacao.html', {'form': form})

def edita_votacao(request, pk):
    votacao = get_object_or_404(Votacao, pk=pk)
    if request.method == "POST":
        form = VotacaoForm(request.POST, instance=votacao)
        if form.is_valid():
            form.save()
            return redirect('lista_votacoes')
    else:
        form = VotacaoForm(instance=votacao)
    return render(request, 'votacao/edita_votacao.html', {'form': form})

def deleta_votacao(request, pk):
    votacao = get_object_or_404(Votacao, pk=pk)
    if request.method == "POST":
        votacao.delete()
        return redirect('lista_votacoes')
    return render(request, 'votacao/deleta_votacao.html', {'votacao': votacao})

def visualiza_votacao(request, pk):
    votacao = get_object_or_404(Votacao, pk=pk)
    return render(request, 'votacao/visualiza_votacao.html', {'votacao': votacao})


#status votacao

def lista_status_votacoes(request):
    status_votacoes = StatusVotacao.objects.all()
    return render(request, 'votacao/lista_status_votacoes.html', {'status_votacoes': status_votacoes})

def novo_status_votacao(request):
    if request.method == "POST":
        form = StatusVotacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_status_votacoes')
    else:
        form = StatusVotacaoForm()
    return render(request, 'votacao/novo_status_votacao.html', {'form': form})

def edita_status_votacao(request, pk):
    status_votacao = get_object_or_404(StatusVotacao, pk=pk)
    if request.method == "POST":
        form = StatusVotacaoForm(request.POST, instance=status_votacao)
        if form.is_valid():
            form.save()
            return redirect('lista_status_votacoes')
    else:
        form = StatusVotacaoForm(instance=status_votacao)
    return render(request, 'votacao/edita_status_votacao.html', {'form': form})

def deleta_status_votacao(request, pk):
    status_votacao = get_object_or_404(StatusVotacao, pk=pk)
    if request.method == "POST":
        status_votacao.delete()
        return redirect('lista_status_votacoes')
    return render(request, 'votacao/deleta_status_votacao.html', {'status_votacao': status_votacao})

def visualiza_status_votacao(request, pk):
    status_votacao = get_object_or_404(StatusVotacao, pk=pk)
    return render(request, 'votacao/visualiza_status_votacao.html', {'status_votacao': status_votacao})
