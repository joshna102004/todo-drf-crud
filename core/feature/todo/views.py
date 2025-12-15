# todo/views.py
from .models import Todo
from .dataclasses import TodoData

def list_todos():
    return Todo.objects.all().order_by("-created_at")

def create_todo(todo_data: TodoData):
    todo = Todo.objects.create(
        title=todo_data.title,
        description=todo_data.description,
        is_completed=todo_data.is_completed
    )
    return todo

def update_todo(todo_instance, todo_data: TodoData):
    todo_instance.title = todo_data.title
    todo_instance.description = todo_data.description
    todo_instance.is_completed = todo_data.is_completed
    todo_instance.save()
    return todo_instance

def delete_todo(todo_instance):
    todo_instance.delete()
