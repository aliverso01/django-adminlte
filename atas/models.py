from django.db import models
from django.urls import reverse

class Ata(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField(auto_now=True)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("atas:detalhes_ata", kwargs={"pk": self.pk})


class Pauta(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField(auto_now=True)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("atas:detalhes_pauta", kwargs={"pk": self.pk})

