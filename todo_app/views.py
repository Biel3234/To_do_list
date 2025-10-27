from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Tarefa
from .forms import TarefaForm

# CRUD para manusear as tasks

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



def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse('Usuario ja existe')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

    return HttpResponse('<h1>Usuario Cadastrado com sucesso<h1>')


def login_usuario(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('nome')
        password = request.POST.get('senha')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse('<h1>Logado com sucesso')
        else:
            return HttpResponse('<h1>Usuario nao existe<h1>')

