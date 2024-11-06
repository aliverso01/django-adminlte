from django.db import models


class Evento(models.Model):
    agenda = models.CharField(max_length=200, null=True, blank=True)
    etiqueta = models.ForeignKey('Etiqueta', on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=200, null=True, blank=True)
    com_quem = models.CharField(max_length=100, null=True, blank=True)
    informacoes = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.agenda.nome} - {self.data} {self.hora}"
    
class Etiqueta(models.Model):
    nome = models.CharField(max_length=200, null=True, blank=True)
    cor = models.CharField(max_length=7, null=True, blank=True) 

    def __str__(self):
        return self.nome