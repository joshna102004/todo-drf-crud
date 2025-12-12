# todo/serializers/request_serializers.py
from rest_framework import serializers

class TodoRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    is_completed = serializers.BooleanField(default=False)
