from django.shortcuts import get_object_or_404

from feature.artist.models import Artist
from feature.artist.serializers.request_serializers import ArtistRequestSerializer


class ArtistView:

    def list(self):
        artists = Artist.objects.all()
        serializer = ArtistRequestSerializer(artists, many=True)
        return serializer.data

    def get(self, artist_id):
        artist = get_object_or_404(Artist, id=artist_id)
        serializer = ArtistRequestSerializer(artist)
        return serializer.data

    def create(self, data):
        serializer = ArtistRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        artist = serializer.save()
        return ArtistRequestSerializer(artist).data

    def update(self, artist_id, data):
        artist = get_object_or_404(Artist, id=artist_id)
        serializer = ArtistRequestSerializer(
            artist, data=data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        artist = serializer.save()
        return ArtistRequestSerializer(artist).data

    def delete(self, artist_id):
        artist = get_object_or_404(Artist, id=artist_id)
        artist.delete()
        return {"message": "Artist deleted successfully"}
