from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario_view, name='calendario'),
    path('carregar_eventos/', views.carregar_eventos, name='carregar_eventos'),
    path('adicionar_evento/', views.adicionar_evento, name='adicionar_evento'),
    path('editar_evento/', views.editar_evento, name='editar_evento'),
    path('deletar_evento/', views.deletar_evento, name='deletar_evento'),
    path('criar_etiqueta/', views.criar_etiqueta, name='criar_etiqueta'),
]
