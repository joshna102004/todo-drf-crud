from rest_framework.response import Response
from rest_framework import status
from math import ceil


# ==========================
# COMMON RESPONSE HELPERS
# ==========================

def success_response(data=None, message="Success", status_code=status.HTTP_200_OK):
    return Response(
        {
            "success": True,
            "message": message,
            "data": data
        },
        status=status_code
    )


def error_response(errors=None, message="Error", status_code=status.HTTP_400_BAD_REQUEST):
    return Response(
        {
            "success": False,
            "message": message,
            "errors": errors
        },
        status=status_code
    )


# ==========================
# PAGINATION UTILITIES
# ==========================

def parse_pagination(request):
    """
    PARSING:
    Read page and page_size from query params
    """
    try:
        page = int(request.query_params.get("page", 1))
    except (ValueError, TypeError):
        page = 1

    try:
        page_size = int(request.query_params.get("page_size", 10))
    except (ValueError, TypeError):
        page_size = 10

    if page < 1:
        page = 1
    if page_size < 1:
        page_size = 10

    return page, page_size


def paginate_queryset(queryset, page, page_size):
    """
    SPLITTING + PAGINATION
    """
    total_items = queryset.count()
    total_pages = ceil(total_items / page_size) if page_size else 1

    start = (page - 1) * page_size
    end = start + page_size

    return {
        "items": queryset[start:end],
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages
        }
    }
