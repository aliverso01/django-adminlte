from django.urls import path
from .views import ListaPostsView, DetalhesPostView, AdicionarPostView, AdicionarRespostaView

app_name = 'forum'

urlpatterns = [
    path('', ListaPostsView.as_view(), name='lista_posts'),
    path('post/<int:pk>/', DetalhesPostView.as_view(), name='detalhes_post'),
    path('post/adicionar/', AdicionarPostView.as_view(), name='adicionar_post'),
    path('post/<int:pk>/responder/', AdicionarRespostaView.as_view(), name='adicionar_resposta'),
]
