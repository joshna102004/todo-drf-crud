from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .views import list_todos, create_todo, update_todo, delete_todo
from .serializers.request_serializers import TodoRequestSerializer
from .serializers.response_serializers import TodoResponseSerializer
from .dataclasses import TodoData
from .models import Todo

from .utils.responses import success_response, error_response
from .utils.pagination import parse_pagination, paginate_queryset


@api_view(["GET", "POST"])
def todo_controller(request):

    # ---------- GET ----------
    if request.method == "GET":
        page, page_size = parse_pagination(request)

        queryset = list_todos()
        paginated = paginate_queryset(queryset, page, page_size)

        data = {
            "todos": TodoResponseSerializer(
                paginated["items"], many=True
            ).data,
            "pagination": paginated["pagination"]
        }

        return success_response(data=data)

    # ---------- POST ----------
    if request.method == "POST":
        serializer = TodoRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return error_response(
                message="Validation failed",
                errors=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        todo_data = TodoData(**serializer.validated_data)
        todo = create_todo(todo_data)

        return success_response(
            data=TodoResponseSerializer(todo).data,
            message="Todo created successfully",
            status_code=status.HTTP_201_CREATED
        )


@api_view(["PUT", "DELETE"])
def todo_detail_controller(request, pk):

    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return error_response(
            message="Todo not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    # ---------- PUT ----------
    if request.method == "PUT":
        serializer = TodoRequestSerializer(data=request.data)

        if not serializer.is_valid():
            return error_response(
                message="Validation failed",
                errors=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        todo_data = TodoData(**serializer.validated_data)
        updated_todo = update_todo(todo, todo_data)

        return success_response(
            data=TodoResponseSerializer(updated_todo).data,
            message="Todo updated successfully"
        )

    # ---------- DELETE ----------
    if request.method == "DELETE":
        delete_todo(todo)
        return Response(status=status.HTTP_204_NO_CONTENT)
