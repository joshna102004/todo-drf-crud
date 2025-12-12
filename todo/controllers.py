# todo/controllers.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .views import list_todos, create_todo, update_todo, delete_todo
from .serializers.request_serializers import TodoRequestSerializer
from .serializers.response_serializers import TodoResponseSerializer
from .dataclasses import TodoData
from .models import Todo

@api_view(["GET", "POST"])
def todo_controller(request):
    if request.method == "GET":
        todos = list_todos()
        return Response(TodoResponseSerializer(todos, many=True).data)

    if request.method == "POST":
        serializer = TodoRequestSerializer(data=request.data)
        if serializer.is_valid():
            todo_data = TodoData(**serializer.validated_data)
            todo = create_todo(todo_data)
            return Response(TodoResponseSerializer(todo).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
def todo_detail_controller(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response({"error": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = TodoRequestSerializer(data=request.data)
        if serializer.is_valid():
            todo_data = TodoData(**serializer.validated_data)
            updated_todo = update_todo(todo, todo_data)
            return Response(TodoResponseSerializer(updated_todo).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        delete_todo(todo)
        return Response(status=status.HTTP_204_NO_CONTENT)
