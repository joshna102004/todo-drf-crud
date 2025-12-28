from django.core.exceptions import ValidationError
from .models import Todo
from .dataclasses import TodoData

def _to_dict(todo: Todo):
    return {
        "id": todo.id,
        "title": todo.title,
        "description": todo.description,
        "is_completed": todo.is_completed,
        "created_at": todo.created_at,
    }

def list_todos():
    return list(
        Todo.objects.all()
        .order_by("-created_at")
        .values("id", "title", "description", "is_completed", "created_at")
    )

def get_todo(todo_id: int):
    try:
        return _to_dict(Todo.objects.get(id=todo_id))
    except Todo.DoesNotExist:
        return None

def create_todo(data: TodoData):
    todo = Todo.objects.create(
        title=data.title,
        description=data.description,
        is_completed=data.is_completed,
    )
    return _to_dict(todo)

def update_todo(todo_id: int, data: TodoData):
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.title = data.title
        todo.description = data.description
        todo.is_completed = data.is_completed
        todo.save()
        return _to_dict(todo)
    except Todo.DoesNotExist:
        return None

def delete_todo(todo_id: int):
    try:
        Todo.objects.get(id=todo_id).delete()
        return True
    except Todo.DoesNotExist:
        return False
