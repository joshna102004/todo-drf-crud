from rest_framework.response import Response

def success_response(data=None, message="Success", status=200):
    """
    Standard success response
    """
    return Response({
        "success": True,
        "message": message,
        "data": data
    }, status=status)


def error_response(message="Error", errors=None, status=400):
    """
    Standard error response
    """
    resp = {
        "success": False,
        "message": message,
    }
    if errors is not None:
        resp["errors"] = errors
    return Response(resp, status=status)
