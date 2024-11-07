# atas/forms.py

from django import forms
from .models import Ata, Pauta
from django_summernote.widgets import SummernoteWidget

class AtaForm(forms.ModelForm):
    class Meta:
        model = Ata
        fields = ['titulo', 'conteudo']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

class PautaForm(forms.ModelForm):
    class Meta:
        model = Pauta
        fields = ['titulo', 'conteudo']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
        }
