from rest_framework import serializers

class TodoPartialUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    is_completed = serializers.BooleanField(required=False)
