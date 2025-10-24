from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Tarefa

# Create your views here.


class Listar_tarefas(ListView):
    model = Tarefa
    context_object_name = 'tarefas'
    template_name = 'tarefa_list.html'
