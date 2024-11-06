# financeiro/models.py

from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_recebimento = models.DateField()
    fonte = models.ForeignKey('FonteReceita', on_delete=models.CASCADE)  # Nova tabela para fontes de receita

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class FonteReceita(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Despesa(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    categoria = models.ForeignKey('CategoriaDespesa', on_delete=models.CASCADE)  # Nova tabela para categorias de despesas

    def __str__(self):
        return f"{self.descricao} - R$ {self.valor}"

class CategoriaDespesa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class FolhaPagamento(models.Model):
    nome_funcionario = models.CharField(max_length=255)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)  # Nova tabela para cargos
    salario_bruto = models.DecimalField(max_digits=10, decimal_places=2)
    encargos = models.DecimalField(max_digits=10, decimal_places=2)
    salario_liquido = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()

    def __str__(self):
        return f"{self.nome_funcionario} - {self.cargo}"

class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Licitacao(models.Model):
    numero_processo = models.CharField(max_length=100)
    objeto = models.TextField()
    valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    data_abertura = models.DateField()
    status = models.ForeignKey('StatusLicitacao', on_delete=models.CASCADE)  # Nova tabela para status de licitações

    def __str__(self):
        return f"Licitação {self.numero_processo} - {self.status}"

class StatusLicitacao(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Contrato(models.Model):
    numero = models.CharField(max_length=100)
    fornecedor = models.CharField(max_length=255)
    objeto = models.TextField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    status = models.ForeignKey('StatusContrato', on_delete=models.CASCADE)  # Nova tabela para status de contratos

    def __str__(self):
        return f"Contrato {self.numero} - {self.fornecedor}"

class StatusContrato(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class PrestacaoContas(models.Model):
    periodo = models.CharField(max_length=50)
    total_receitas = models.DecimalField(max_digits=12, decimal_places=2)
    total_despesas = models.DecimalField(max_digits=12, decimal_places=2)
    data_envio = models.DateField()

    def __str__(self):
        return f"Prestação de Contas - {self.periodo}"
