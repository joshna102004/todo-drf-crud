from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .serializers import CreateUserSerializer, UpdateUserSerializer

@swagger_auto_schema(
    method='get',
    responses={200: "Users fetched successfully"}
)
@api_view(["GET"])
def get_users(request):
    return Response(
        {
            "users": [
                {"id": 1, "name": "Steve", "email": "steve@test.com"},
                {"id": 2, "name": "Alex", "email": "alex@test.com"},
            ]
        },
        status=status.HTTP_200_OK
    )
@swagger_auto_schema(
    method='get',
    responses={200: "User fetched successfully", 404: "User not found"}
)
@api_view(["GET"])
def get_user(request, user_id):
    return Response(
        {"id": user_id, "name": "Steve", "email": "steve@test.com"},
        status=status.HTTP_200_OK
    )

@api_view(["GET"])
def health_check(request):
    """
    Health Check API

    Returns server status.
    """
    return Response({"status": "OK"}, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_user(request):
    """
    Create User API

    Accepts user data and creates a new user.
    """
    return Response(
        {"message": "User created successfully"},


        status=status.HTTP_201_CREATED
    )
@swagger_auto_schema(
    method='put',
    request_body=UpdateUserSerializer,
    responses={200: "User updated successfully"}
)
@api_view(["PUT"])
def update_user(request, user_id):
    serializer = UpdateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    return Response(
        {
            "message": "User updated successfully",
            "data": serializer.validated_data
        },
        status=status.HTTP_200_OK
    )
@swagger_auto_schema(
    method='patch',
    request_body=UpdateUserSerializer,
    responses={200: "User partially updated"}
)
@api_view(["PATCH"])
def partial_update_user(request, user_id):
    serializer = UpdateUserSerializer(data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)

    return Response(
        {
            "message": "User partially updated",
            "data": serializer.validated_data
        },
        status=status.HTTP_200_OK
    )
@swagger_auto_schema(
    method='delete',
    responses={204: "User deleted successfully"}
)
@api_view(["DELETE"])
def delete_user(request, user_id):
    return Response(
        {"message": "User deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )
