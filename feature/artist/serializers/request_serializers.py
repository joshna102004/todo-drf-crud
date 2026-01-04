from rest_framework import serializers
from feature.artist.models.artist_model import Artist

class ArtistRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
