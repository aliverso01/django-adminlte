from django.urls import path
from . import views

urlpatterns = [
    path('kanban/', views.kanban_board, name='kanban_board'),
    path('update-card/', views.update_card_position, name='update_card_position'),
]
