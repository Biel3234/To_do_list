from django.urls import path
from .views import Listar_tarefas

urlpatterns = [
    path('listar/', Listar_tarefas.as_view())
]
