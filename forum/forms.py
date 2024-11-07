from django import forms
from .models import Post, Resposta

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']

class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ['conteudo']
