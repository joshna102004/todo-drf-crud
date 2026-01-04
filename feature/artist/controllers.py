from rest_framework.decorators import api_view
from feature.artist.views import ArtistView
from feature.artist.serializers.response_serializers import response_serializer

view = ArtistView()

@api_view(['GET'])
@response_serializer
def list_artists(request):
    return view.list()

@api_view(['GET'])
@response_serializer
def get_artist(request, artist_id):
    return view.get(artist_id)

@api_view(['POST'])
@response_serializer
def create_artist(request):
    return view.create(request.data)

@api_view(['PUT'])
@response_serializer
def update_artist(request, artist_id):
    return view.update(artist_id, request.data)

@api_view(['DELETE'])
@response_serializer
def delete_artist(request, artist_id):
    return view.delete(artist_id)
