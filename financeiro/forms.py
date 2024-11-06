from django import forms
from .models import (
    Receita, Despesa, FonteReceita, CategoriaDespesa,
    FolhaPagamento, Licitacao, Contrato, PrestacaoContas
)

# Formulário para Receita
class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'data_recebimento', 'fonte']
        widgets = {
            'data_recebimento': forms.DateInput(attrs={'type': 'date'}),
            'valor': forms.NumberInput(attrs={'step': '0.01'}),
        }

# Formulário para Despesa
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'data_pagamento', 'categoria']
        widgets = {
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
            'valor': forms.NumberInput(attrs={'step': '0.01'}),
        }

# Formulário para Fonte de Receita
class FonteReceitaForm(forms.ModelForm):
    class Meta:
        model = FonteReceita
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da fonte de receita'}),
        }

# Formulário para Categoria de Despesa
class CategoriaDespesaForm(forms.ModelForm):
    class Meta:
        model = CategoriaDespesa
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome da categoria de despesa'}),
        }

# Formulário para Folha de Pagamento
class FolhaPagamentoForm(forms.ModelForm):
    class Meta:
        model = FolhaPagamento
        fields = ['nome_funcionario', 'cargo', 'salario_bruto', 'encargos', 'salario_liquido', 'data_pagamento']
        widgets = {
            'data_pagamento': forms.DateInput(attrs={'type': 'date'}),
            'salario_bruto': forms.NumberInput(attrs={'step': '0.01'}),
            'encargos': forms.NumberInput(attrs={'step': '0.01'}),
            'salario_liquido': forms.NumberInput(attrs={'step': '0.01'}),
        }

# Formulário para Licitação
class LicitacaoForm(forms.ModelForm):
    class Meta:
        model = Licitacao
        fields = ['numero_processo', 'objeto', 'valor_estimado', 'data_abertura', 'status']
        widgets = {
            'data_abertura': forms.DateInput(attrs={'type': 'date'}),
            'valor_estimado': forms.NumberInput(attrs={'step': '0.01'}),
        }

# Formulário para Contrato
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['numero', 'fornecedor', 'objeto', 'valor_total', 'data_inicio', 'data_fim', 'status']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'type': 'date'}),
            'valor_total': forms.NumberInput(attrs={'step': '0.01'}),
        }

# Formulário para Prestação de Contas
class PrestacaoContasForm(forms.ModelForm):
    class Meta:
        model = PrestacaoContas
        fields = ['periodo', 'total_receitas', 'total_despesas', 'data_envio']
        widgets = {
            'data_envio': forms.DateInput(attrs={'type': 'date'}),
            'total_receitas': forms.NumberInput(attrs={'step': '0.01'}),
            'total_despesas': forms.NumberInput(attrs={'step': '0.01'}),
        }
