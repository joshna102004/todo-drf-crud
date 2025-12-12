from rest_framework import serializers

class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    is_completed = serializers.BooleanField(default=False)

class TodoUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    is_completed = serializers.BooleanField(required=False)
