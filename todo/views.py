from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import controllers
from .models import Todo
from .serializers.response import TodoResponseSerializer


@api_view(["GET", "POST"])
def todo_list_create(request):
    if request.method == "GET":
        qs = Todo.objects.all().order_by("-created_at")
        return Response(TodoResponseSerializer(qs, many=True).data)

    # FIXED: pass request.data
    todo_dc = controllers.prepare_create(request.data)

    todo = Todo.create_from_dataclass(todo_dc)
    return Response(TodoResponseSerializer(todo).data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def todo_detail(request, pk):
    todo = Todo.get_or_404(pk)

    if request.method == "GET":
        return Response(TodoResponseSerializer(todo).data)

    if request.method == "DELETE":
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == "PUT":
        update_dc = controllers.prepare_full_update(request.data)
        updated = todo.apply_update_dataclass(update_dc)
        return Response(TodoResponseSerializer(updated).data)

    if request.method == "PATCH":
        update_dc = controllers.prepare_partial_update(request.data)
        updated = todo.apply_update_dataclass(update_dc)
        return Response(TodoResponseSerializer(updated).data)
