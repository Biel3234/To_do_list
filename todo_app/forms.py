from django import forms
from .models import Tarefa


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa

        fields = ['nome_tarefa', 'descricao']

        labels = {
            'nome_tarefa': 'Nome da Tarefa',
            'descricao': 'Descrição'
        }

        widgets = {
            'nome_tarefa': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'})
        }