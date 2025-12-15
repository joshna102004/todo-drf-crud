from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers.request_serializers import TodoRequestSerializer
from .serializers.response_serializers import TodoResponseSerializer
from .dataclasses import TodoData
from .models import Todo
from .views import (
    list_todos,
    get_todo,
    create_todo,
    update_todo,
    delete_todo,
)

from .utils.responses import success_response, error_response
from .utils.pagination import parse_pagination, paginate_queryset


# ---------- CREATE ----------
@api_view(["POST"])
def create_todo_controller(request):
    serializer = TodoRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response(
            "Validation failed",
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

    todo_data = TodoData(**serializer.validated_data)
    todo = create_todo(todo_data)

    return success_response(
        TodoResponseSerializer(todo).data,
        "Todo created successfully",
        status.HTTP_201_CREATED
    )


# ---------- LIST ----------
@api_view(["GET"])
def list_todos_controller(request):
    page, page_size = parse_pagination(request)

    queryset = list_todos()
    paginated = paginate_queryset(queryset, page, page_size)

    return success_response({
        "todos": TodoResponseSerializer(paginated["items"], many=True).data,
        "pagination": paginated["pagination"],
    })


# ---------- GET ----------
@api_view(["GET"])
def get_todo_controller(request):
    todo_id = request.GET.get("id")

    if not todo_id:
        return error_response("Todo id is required")

    try:
        todo = get_todo(todo_id)
    except Todo.DoesNotExist:
        return error_response("Todo not found", status.HTTP_404_NOT_FOUND)

    return success_response(TodoResponseSerializer(todo).data)


# ---------- UPDATE ----------
@api_view(["PUT"])
def update_todo_controller(request):
    todo_id = request.GET.get("id")

    if not todo_id:
        return error_response("Todo id is required")

    try:
        todo = get_todo(todo_id)
    except Todo.DoesNotExist:
        return error_response("Todo not found", status.HTTP_404_NOT_FOUND)

    serializer = TodoRequestSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response(
            "Validation failed",
            serializer.errors,
            status.HTTP_400_BAD_REQUEST
        )

    todo_data = TodoData(**serializer.validated_data)
    updated = update_todo(todo, todo_data)

    return success_response(
        TodoResponseSerializer(updated).data,
        "Todo updated successfully"
    )


# ---------- DELETE ----------
@api_view(["DELETE"])
def delete_todo_controller(request):
    todo_id = request.GET.get("id")

    if not todo_id:
        return error_response("Todo id is required")

    try:
        todo = get_todo(todo_id)
    except Todo.DoesNotExist:
        return error_response("Todo not found", status.HTTP_404_NOT_FOUND)

    delete_todo(todo)
    return Response(status=status.HTTP_204_NO_CONTENT)
