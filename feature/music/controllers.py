from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers.request_serializers import MusicRequestSerializer
from .views import (
    list_music,
    get_music,
    create_music,
    update_music,
    delete_music,
)

from feature.common.utils.pagination import parse_pagination, paginate_queryset
from feature.common.utils.responses import success_response, error_response
from feature.common.swagger import (
    music_list_swagger,
    music_get_swagger,
    music_create_swagger,
    music_update_swagger,
    music_delete_swagger,
)


class MusicController:

    # -------- CREATE --------
    @staticmethod
    @api_view(["POST"])
    @music_create_swagger(MusicRequestSerializer)
    def create(request):
        serializer = MusicRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(
                message="Validation failed",
                errors=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        data = serializer.to_dataclass()
        result = create_music(data)

        if isinstance(result, dict) and "error" in result:
            return error_response(result["error"])

        return success_response(
            data=result,
            message="Music created successfully",
            status_code=status.HTTP_201_CREATED
        )

    # -------- LIST --------
    @staticmethod
    @api_view(["GET"])
    @music_list_swagger()
    def list(request):
        page, page_size = parse_pagination(request)
        music_list = list_music()
        paginated = paginate_queryset(music_list, page, page_size)

        return success_response(
            data={
                "items": paginated["items"],
                "pagination": paginated["pagination"],
            },
            message="Music list fetched successfully"
        )

    # -------- GET ONE --------
    @staticmethod
    @api_view(["GET"])
    @music_get_swagger()
    def get_one(request, id):
        result = get_music(id)
        if not result:
            return error_response(
                message="Music not found",
                status_code=status.HTTP_404_NOT_FOUND
            )
        return success_response(data=result)

    # -------- UPDATE --------
    @staticmethod
    @api_view(["PUT"])
    @music_update_swagger(MusicRequestSerializer)
    def update(request, id):
        serializer = MusicRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return error_response(
                message="Validation failed",
                errors=serializer.errors,
                status_code=status.HTTP_400_BAD_REQUEST
            )

        data = serializer.to_dataclass()
        result = update_music(id, data)

        if result is None:
            return error_response(
                message="Music not found",
                status_code=status.HTTP_404_NOT_FOUND
            )

        if isinstance(result, dict) and "error" in result:
            return error_response(result["error"])

        return success_response(
            data=result,
            message="Music updated successfully"
        )

    # -------- DELETE --------
    @staticmethod
    @api_view(["DELETE"])
    @music_delete_swagger()
    def delete(request, id):
        success = delete_music(id)
        if not success:
            return error_response(
                message="Music not found",
                status_code=status.HTTP_404_NOT_FOUND
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
