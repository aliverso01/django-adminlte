from django import forms
from .models import Veiculo, SolicitaCombustivel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['tipo', 'marca', 'modelo', 'placa', 'status_disponibilidade', 'data_aquisicao']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

class SolicitaCombustivelForm(forms.ModelForm):
    class Meta:
        model = SolicitaCombustivel
        fields = ['veiculo', 'responsavel', 'solicitante', 'objetivo', 'litros', 'valor_litro', 'data_saida', 'data_retorno', 'comprovante']
        widgets = {
            'data_saida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_retorno': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'litros': forms.NumberInput(attrs={'step': '0.01'}),
            'valor_litro': forms.NumberInput(attrs={'step': '0.01'}),
        }