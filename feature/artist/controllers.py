from rest_framework.decorators import api_view
from feature.artist.views import ArtistView
from feature.artist.serializers.response_serializers import response_serializer
from feature.artist.serializers.request_serializers import ArtistRequestSerializer
from feature.common.swagger import (
    artist_list_swagger,
    artist_get_swagger,
    artist_create_swagger,
    artist_update_swagger,
    artist_delete_swagger,
)

view = ArtistView()


@api_view(['GET'])
@artist_list_swagger()
@response_serializer
def list_artists(request):
    return view.list()


@api_view(['GET'])
@artist_get_swagger()
@response_serializer
def get_artist(request, artist_id):
    return view.get(artist_id)


@api_view(['POST'])
@artist_create_swagger(ArtistRequestSerializer)
@response_serializer
def create_artist(request):
    return view.create(request.data)


@api_view(['PUT'])
@artist_update_swagger(ArtistRequestSerializer)
@response_serializer
def update_artist(request, artist_id):
    return view.update(artist_id, request.data)


@api_view(['DELETE'])
@artist_delete_swagger()
@response_serializer
def delete_artist(request, artist_id):
    return view.delete(artist_id)
