from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Board, Card
from .forms import BoardForm, CardForm
import json
from django.db import transaction

def kanban_board(request):
    """Renderiza a página Kanban com os boards e cards, além dos formulários."""
    boards = Board.objects.prefetch_related('cards').all()
    board_form = BoardForm()
    card_form = CardForm()

    if request.method == 'POST':
        if 'board_submit' in request.POST:
            board_form = BoardForm(request.POST)
            if board_form.is_valid():
                board_form.save()
                return redirect('kanban_board')

        elif 'card_submit' in request.POST:
            card_form = CardForm(request.POST)
            if card_form.is_valid():
                card_form.save()
                return redirect('kanban_board')

    return render(request, 'marketing/kanban_board.html', {
        'boards': boards,
        'board_form': board_form,
        'card_form': card_form
    })

@csrf_exempt
def update_card_position(request):
    """Atualiza a posição e o board dos cards via drag-and-drop."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            with transaction.atomic():
                for item in data:
                    card = get_object_or_404(Card, id=item['id'])
                    card.board_id = item['board']
                    card.position = item['position']
                    card.save()
                    
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'failed', 'message': 'Invalid request'}, status=400)
