from django import forms
from .models import Votacao, StatusVotacao

class VotacaoForm(forms.ModelForm):
    class Meta:
        model = Votacao
        fields = '__all__'

class StatusVotacaoForm(forms.ModelForm):
    class Meta:
        model = StatusVotacao
        fields = '__all__'
    