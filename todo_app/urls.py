from django.urls import path
from .views import Listar_tarefas, Criar_tarefa, Exibir_tarefa, Deletar_tarefa, Editar_tarefa

app_name = 'todo'

urlpatterns = [
    path('listar/', Listar_tarefas.as_view(), name='listar'),
    path('criar/', Criar_tarefa.as_view(), name='criar'),
    path('detalhar/<int:pk>/', Exibir_tarefa.as_view(), name='detalhar'),
    path('deletar/<int:pk>/', Deletar_tarefa.as_view(), name='deletar'),
    path('editar/<int:pk>/', Editar_tarefa.as_view(), name='editar'),
]
