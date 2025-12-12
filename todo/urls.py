# todo/urls.py
from django.urls import path
from .controllers import todo_controller, todo_detail_controller

urlpatterns = [
    path("todos/", todo_controller, name="todo_list_create"),
    path("todos/<int:pk>/", todo_detail_controller, name="todo_detail"),
]
