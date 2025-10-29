from django.db import models
from django.contrib.auth.models import User


class Tarefa(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas', null=False)
    nome_tarefa = models.CharField(max_length=100)
    descricao = models.TextField(max_length=300)
    data_criacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_tarefa