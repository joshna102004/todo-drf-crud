from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers.request_serializers import TodoRequestSerializer
from .dataclasses import TodoData
from .views import (
    list_todos,
    get_todo,
    create_todo,
    update_todo,
    delete_todo,
)


from core.common.utils.pagination import parse_pagination, paginate_queryset
from core.common.utils.responses import success_response, error_response



@api_view(["POST"])
def create_todo_controller(request):
    serializer = TodoRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    data = TodoData(**serializer.validated_data)
    result = create_todo(data)

    if "error" in result:
        return error_response(result["error"])

    return success_response(result, "Todo created", status.HTTP_201_CREATED)


@api_view(["GET"])
def list_todos_controller(request):
    page, page_size = parse_pagination(request)
    todos = list_todos()
    paginated = paginate_queryset(todos, page, page_size)

    return success_response({
        "todos": paginated["items"],
        "pagination": paginated["pagination"],
    })


@api_view(["GET"])
def get_todo_controller(request):
    todo_id = request.GET.get("id")
    if not todo_id:
        return error_response("Todo id is required")

    result = get_todo(todo_id)
    if not result:
        return error_response("Todo not found", status.HTTP_404_NOT_FOUND)

    return success_response(result)


@api_view(["PUT"])
def update_todo_controller(request):
    todo_id = request.GET.get("id")
    if not todo_id:
        return error_response("Todo id is required")

    serializer = TodoRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    data = TodoData(**serializer.validated_data)
    result = update_todo(todo_id, data)

    if result is None:
        return error_response("Todo not found", status.HTTP_404_NOT_FOUND)

    if "error" in result:
        return error_response(result["error"])

    return success_response(result, "Todo updated")


@api_view(["DELETE"])
def delete_todo_controller(request):
    todo_id = request.GET.get("id")
    if not todo_id:
        return error_response("Todo id is required")

    success = delete_todo(todo_id)
    if not success:
        return error_response("Todo not found", status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_204_NO_CONTENT)
