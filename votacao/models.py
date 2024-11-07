from django.db import models
from propostas.models import Proposta
from django.contrib.auth.models import User



class Votacao(models.Model):
    numero_protocolo = models.CharField(max_length=200, null=True, blank=True)
    proposta = models.ForeignKey(Proposta, on_delete=models.CASCADE)
    status = models.ForeignKey('StatusVotacao', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class StatusVotacao(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status