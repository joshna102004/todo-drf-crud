from rest_framework import serializers
from ..models import Music

class MusicResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["id", "title", "artist", "duration", "created_at"]
