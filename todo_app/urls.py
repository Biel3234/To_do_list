from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('listar/', views.Listar_tarefas.as_view(), name='listar'),
    path('criar/', views.Criar_tarefa.as_view(), name='criar'),
    path('detalhar/<int:pk>/', views.Exibir_tarefa.as_view(), name='detalhar'),
    path('deletar/<int:pk>/', views.Deletar_tarefa.as_view(), name='deletar'),
    path('editar/<int:pk>/', views.Editar_tarefa.as_view(), name='editar'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro')
]
