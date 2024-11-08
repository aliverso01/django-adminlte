from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Resposta
from .forms import PostForm, RespostaForm

class ListaPostsView(ListView):
    model = Post
    template_name = 'forum/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-criado_em']

class DetalhesPostView(DetailView):
    model = Post
    template_name = 'forum/detalhes_post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resposta_form'] = RespostaForm()
        return context

class AdicionarPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/form_post.html'
    success_url = reverse_lazy('forum:lista_posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class AdicionarRespostaView(LoginRequiredMixin, CreateView):
    model = Resposta
    form_class = RespostaForm
    template_name = 'forum/form_resposta.html'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum:detalhes_post', kwargs={'pk': self.object.post.pk})
