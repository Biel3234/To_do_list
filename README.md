# To-do List

Aplicação web simples de lista de tarefas construída com Django.

A aplicação foi deployada em: https://to-do-list-h4k9.onrender.com/

## Descrição

Este projeto permite que usuários se cadastrem, façam login e gerenciem tarefas (criar, editar, deletar, marcar como concluída). O front-end utiliza Django Templates e um CSS central (`todo_app/static/css.css`) para manter o estilo consistente.

## Funcionalidades

- Cadastro de usuário
- Login / Logout
- CRUD de tarefas (criar, listar, editar, deletar)
- Marcar tarefas como concluídas/pendentes
- Página de detalhes da tarefa

## Tecnologias

- Python 3.x
- Django
- SQLite (padrão de desenvolvimento)
- HTML/CSS (Django Templates)

## Como rodar localmente

1. Clone o repositório:

```powershell
git clone https://github.com/Biel3234/To_do_list.git
cd To_do_list
```

2. Crie e ative um ambiente virtual (Windows):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Instale dependências:

```powershell
pip install -r requirements.txt
```

4. Execute migrações e rode o servidor:

```powershell
python manage.py migrate
python manage.py runserver
```

Acesse em `http://127.0.0.1:8000/`.

## Notas sobre o deploy

A aplicação foi deployada no Render. URL pública:

https://to-do-list-h4k9.onrender.com/

## Estrutura do projeto (resumida)

- `todo_app/` - app Django com modelos, views, templates e static
- `todo_project/` - configurações do Django
- `db.sqlite3` - banco local (não recomendado com dados sensíveis)

## Como contribuir

1. Fork e clone o repositório
2. Crie uma branch para sua feature
3. Faça commits pequenos e claros
4. Abra um Pull Request

## Autor

Biel3234

---