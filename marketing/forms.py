from django import forms
from .models import Board, Card

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter board name'}),
        }

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'description', 'board']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter card title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'board': forms.Select(attrs={'class': 'form-control'}),
        }
