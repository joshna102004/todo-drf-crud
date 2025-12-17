from django.core.paginator import Paginator


def parse_pagination(request):
    page = int(request.GET.get("page", 1))
    page_size = int(request.GET.get("page_size", 10))
    return page, page_size


def paginate_queryset(queryset, page, page_size):
    paginator = Paginator(queryset, page_size)
    page_obj = paginator.get_page(page)

    return {
        "items": page_obj.object_list,
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_pages": paginator.num_pages,
            "total_items": paginator.count,
        }
    }
