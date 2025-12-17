from rest_framework import serializers
from ..dataclasses import MusicData

class MusicRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    artist = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required")
        if len(value) > 200:
            raise serializers.ValidationError("Title too long")
        return value

    def validate_artist(self, value):
        if not value:
            raise serializers.ValidationError("Artist is required")
        if len(value) > 100:
            raise serializers.ValidationError("Artist too long")
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be positive")
        return value

    def to_dataclass(self) -> MusicData:
        return MusicData(**self.validated_data)
