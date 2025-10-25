from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
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

class Exibir_tarefa(DetailView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'tarefa_detail.html'

class Deletar_tarefa(DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'tarefa_confirmar_delete.html'
    success_url = reverse_lazy('todo:listar')

class Editar_tarefa(UpdateView):
    model = Tarefa
    context_object_name = 'tarefa'
    form_class = TarefaForm
    template_name = 'tarefa_update.html'
    success_url = reverse_lazy('todo:listar')
