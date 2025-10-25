from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.


class Listar_tarefas(ListView):
    model = Tarefa
    context_object_name = 'tarefas'
    template_name = 'tarefa_list.html'

class Criar_tarefa(CreateView):
    model = Tarefa
    form_class = TarefaForm
    context_object_name = 'formulario'
    template_name = 'tarefa_create.html'
    success_url = reverse_lazy('todo:listar')
