from django import forms
from .models import Proposta
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_summernote.widgets import SummernoteWidget

class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = ['titulo', 'descricao']

    def __init__(self, *args, **kwargs):
        super(PropostaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar', css_class='btn btn-success'))