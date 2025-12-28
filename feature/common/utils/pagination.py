from django.core.paginator import Paginator, EmptyPage
from rest_framework.exceptions import ValidationError


def parse_pagination(request):
    """
    Read page & page_size from query params
    """
    try:
        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 10))
    except ValueError:
        raise ValidationError("page and page_size must be integers")

    if page <= 0 or page_size <= 0:
        raise ValidationError("page and page_size must be greater than zero")

    return page, page_size


def paginate_queryset(queryset, page, page_size):
    """
    Paginate a queryset
    """
    paginator = Paginator(queryset, page_size)

    try:
        paginated_data = paginator.page(page)
    except EmptyPage:
        return [], paginator.count

    return paginated_data.object_list, paginator.count
