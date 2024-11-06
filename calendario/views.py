from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Evento, Etiqueta
import json

def calendario_view(request):
    """Renderiza a página do calendário."""
    etiquetas = Etiqueta.objects.all()
    return render(request, 'calendario/calendario.html', {'draggable_events': etiquetas})

def carregar_eventos(request):
    """Retorna os eventos em formato JSON para o FullCalendar."""
    eventos = Evento.objects.all()
    eventos_json = [
        {
            'id': evento.id,
            'title': evento.agenda,
            'start': f"{evento.data}T{evento.hora}",
            'extendedProps': {
                'etiqueta_id': evento.etiqueta.id if evento.etiqueta else None,
                'local': evento.local,
                'com_quem': evento.com_quem,
                'informacoes': evento.informacoes,
            },
            'backgroundColor': evento.etiqueta.cor if evento.etiqueta else '#0073b7',
            'borderColor': evento.etiqueta.cor if evento.etiqueta else '#0073b7',
        }
        for evento in eventos
    ]
    return JsonResponse(eventos_json, safe=False)

@csrf_exempt
def adicionar_evento(request):
    """Cria um novo evento a partir do modal."""
    if request.method == 'POST':
        data = json.loads(request.body)
        etiqueta = get_object_or_404(Etiqueta, id=data.get('etiqueta_id'))
        evento = Evento.objects.create(
            agenda=data.get('agenda'),
            etiqueta=etiqueta,
            data=data.get('data'),
            hora=data.get('hora'),
            local=data.get('local'),
            com_quem=data.get('com_quem'),
            informacoes=data.get('informacoes'),
        )
        return JsonResponse({'status': 'success', 'evento_id': evento.id})
    return JsonResponse({'status': 'failed', 'message': 'Método inválido'}, status=400)

@csrf_exempt
def editar_evento(request):
    """Edita um evento existente."""
    if request.method == 'POST':
        data = json.loads(request.body)
        evento = get_object_or_404(Evento, id=data.get('id'))
        evento.agenda = data.get('agenda')
        evento.etiqueta = get_object_or_404(Etiqueta, id=data.get('etiqueta_id'))
        evento.data = data.get('data')
        evento.hora = data.get('hora')
        evento.local = data.get('local')
        evento.com_quem = data.get('com_quem')
        evento.informacoes = data.get('informacoes')
        evento.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed', 'message': 'Método inválido'}, status=400)

@csrf_exempt
def deletar_evento(request):
    """Exclui um evento existente."""
    if request.method == 'POST':
        data = json.loads(request.body)
        evento = get_object_or_404(Evento, id=data.get('id'))
        evento.delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed', 'message': 'Método inválido'}, status=400)

@csrf_exempt
def criar_etiqueta(request):
    """Cria uma nova etiqueta."""
    if request.method == 'POST':
        data = json.loads(request.body)
        nome = data.get('nome')
        cor = data.get('cor')
        etiqueta = Etiqueta.objects.create(nome=nome, cor=cor)
        return JsonResponse({'status': 'success', 'id': etiqueta.id, 'nome': etiqueta.nome, 'cor': etiqueta.cor})
    return JsonResponse({'status': 'failed', 'message': 'Método inválido'}, status=400)
