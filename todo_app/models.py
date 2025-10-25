from django.db import models
# Create your models here.

class User(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas', null=True)
    nome_tarefa = models.CharField(max_length=100)
    descricao = models.TextField(max_length=300)
    data_criacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_tarefa