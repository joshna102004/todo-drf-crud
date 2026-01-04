from rest_framework.response import Response
from functools import wraps

def response_serializer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        return Response({
            "status": "success",
            "data": data
        })
    return wrapper
