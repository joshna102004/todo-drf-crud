from rest_framework import serializers
from ..dataclasses import TodoData


class TodoRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    is_completed = serializers.BooleanField(default=False)

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title is required")
        if len(value) > 200:
            raise serializers.ValidationError("Title must be at most 200 characters")
        return value

    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Description is required")
        return value

    def create_dataclass(self):
        """
        Convert validated data to TodoData
        """
        return TodoData(**self.validated_data)
