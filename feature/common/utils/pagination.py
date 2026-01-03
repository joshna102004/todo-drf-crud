from django.core.paginator import Paginator, EmptyPage
from rest_framework.exceptions import ValidationError


def parse_pagination(request):
    try:
        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 10))
    except ValueError:
        page = 1
        page_size = 10

    if page <= 0:
        page = 1
    if page_size <= 0:
        page_size = 10

    return page, page_size


def paginate_queryset(queryset, page, page_size):
    paginator = Paginator(queryset, page_size)

    try:
        page_obj = paginator.page(page)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return {
        "items": list(page_obj.object_list),
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": paginator.count,
            "total_pages": paginator.num_pages,
        },
    }
