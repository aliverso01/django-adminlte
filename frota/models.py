from django.db import models
from decimal import Decimal

class Veiculo(models.Model):
    TIPO_VEICULO_CHOICES = [
        ('Proprio', 'Próprio'),
        ('Alugado', 'Alugado'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_VEICULO_CHOICES)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    status_disponibilidade = models.BooleanField(default=True)
    data_aquisicao = models.DateField()

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

class SolicitaCombustivel(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    responsavel = models.CharField(max_length=100)
    solicitante = models.CharField(max_length=100)
    objetivo = models.TextField()
    litros = models.DecimalField(max_digits=5, decimal_places=2)
    valor_litro = models.DecimalField(max_digits=5, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Ajustado para 10 dígitos
    data_saida = models.DateTimeField()
    data_retorno = models.DateTimeField()
    comprovante = models.FileField(upload_to='comprovantes/')

    def save(self, *args, **kwargs):
        self.valor_total = Decimal(self.litros) * Decimal(self.valor_litro)  # Calcula valor total
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.veiculo} - {self.data_saida.strftime('%d/%m/%Y %H:%M')}"