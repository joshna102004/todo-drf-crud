from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers.request_serializers import MusicRequestSerializer
from .views import list_music, get_music, create_music, update_music, delete_music
from .utils.responses import success_response, error_response
from .utils.pagination import parse_pagination, paginate_queryset

@api_view(["POST"])
def create_music_controller(request):
    serializer = MusicRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    data = serializer.to_dataclass()
    result = create_music(data)

    if "error" in result:
        return error_response(result["error"])

    return success_response(result, "Music created", status.HTTP_201_CREATED)


@api_view(["GET"])
def list_music_controller(request):
    page, page_size = parse_pagination(request)
    music_list = list_music()
    paginated = paginate_queryset(music_list, page, page_size)
    return success_response({
        "music": paginated["items"],
        "pagination": paginated["pagination"]
    })


@api_view(["GET"])
def get_music_controller(request):
    music_id = request.GET.get("id")
    if not music_id:
        return error_response("Music id is required")

    result = get_music(music_id)
    if not result:
        return error_response("Music not found", status.HTTP_404_NOT_FOUND)

    return success_response(result)


@api_view(["PUT"])
def update_music_controller(request):
    music_id = request.GET.get("id")
    if not music_id:
        return error_response("Music id is required")

    serializer = MusicRequestSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response("Validation failed", serializer.errors)

    data = serializer.to_dataclass()
    result = update_music(music_id, data)
    if result is None:
        return error_response("Music not found", status.HTTP_404_NOT_FOUND)
    if "error" in result:
        return error_response(result["error"])

    return success_response(result, "Music updated")


@api_view(["DELETE"])
def delete_music_controller(request):
    music_id = request.GET.get("id")
    if not music_id:
        return error_response("Music id is required")

    success = delete_music(music_id)
    if not success:
        return error_response("Music not found", status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_204_NO_CONTENT)
