from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(default=now)

    def __str__(self):
        return self.titulo

class Resposta(models.Model):
    post = models.ForeignKey(Post, related_name='respostas', on_delete=models.CASCADE)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(default=now)

    def __str__(self):
        return f"Resposta de {self.autor} em {self.post.titulo}"
