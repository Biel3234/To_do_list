from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tarefa
from .forms import TarefaForm

# CRUD para manusear as tasks


class Requer_login(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class Listar_tarefas(Requer_login, ListView):
    model = Tarefa
    context_object_name = 'tarefas'
    template_name = 'tarefa_list.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)

class Criar_tarefa(Requer_login, CreateView):
    model = Tarefa
    form_class = TarefaForm
    context_object_name = 'formulario'
    template_name = 'tarefa_create.html'
    success_url = reverse_lazy('todo:listar')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class Exibir_tarefa(Requer_login, DetailView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'tarefa_detail.html'

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)

class Deletar_tarefa(Requer_login, DeleteView):
    model = Tarefa
    context_object_name = 'tarefa'
    template_name = 'tarefa_confirmar_delete.html'
    success_url = reverse_lazy('todo:listar')

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)

class Editar_tarefa(Requer_login, UpdateView):
    model = Tarefa
    context_object_name = 'tarefa'
    form_class = TarefaForm
    template_name = 'tarefa_update.html'
    success_url = reverse_lazy('todo:listar')

    def get_queryset(self):
        return Tarefa.objects.filter(usuario=self.request.user)


def cadastrar_usuario(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        user = User.objects.filter(username = username).first()

        if user:
            return HttpResponse(render(request, 'usuario_ja_existe.html'))
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

    return redirect('todo:logar')


def login_usuario(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('nome')
        password = request.POST.get('senha')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todo:listar')
        else:
            return HttpResponse('<h1>Usuario nao existe<h1>')
        
def deslogar(request):
    logout(request)
    return redirect('todo:logar')

def alterar_status(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.concluida = not tarefa.concluida  # alterna True/False
    tarefa.save()
    return redirect('todo:listar')  # volta pra lista de tarefas

