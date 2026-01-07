from drf_spectacular.utils import extend_schema


# ---------- ARTIST ----------
def artist_list_swagger():
    return extend_schema(
        tags=["Artist"],
        summary="List artists",
        description="Get all artists",
        responses={200: dict}
    )


def artist_get_swagger():
    return extend_schema(
        tags=["Artist"],
        summary="Get artist",
        description="Get artist by ID",
        responses={200: dict, 404: dict}
    )


def artist_create_swagger(request_serializer):
    return extend_schema(
        tags=["Artist"],
        summary="Create artist",
        description="Create new artist",
        request=request_serializer,
        responses={201: dict, 400: dict}
    )


def artist_update_swagger(request_serializer):
    return extend_schema(
        tags=["Artist"],
        summary="Update artist",
        description="Update artist by ID",
        request=request_serializer,
        responses={200: dict, 400: dict, 404: dict}
    )


def artist_delete_swagger():
    return extend_schema(
        tags=["Artist"],
        summary="Delete artist",
        description="Delete artist by ID",
        responses={204: None, 404: dict}
    )


# ---------- MUSIC ----------
def music_list_swagger():
    return extend_schema(
        tags=["Music"],
        summary="List music",
        description="Get all music",
        responses={200: dict}
    )


def music_get_swagger():
    return extend_schema(
        tags=["Music"],
        summary="Get music",
        description="Get music by ID",
        responses={200: dict, 404: dict}
    )


def music_create_swagger(request_serializer):
    return extend_schema(
        tags=["Music"],
        summary="Create music",
        description="Create new music",
        request=request_serializer,
        responses={201: dict, 400: dict}
    )


def music_update_swagger(request_serializer):
    return extend_schema(
        tags=["Music"],
        summary="Update music",
        description="Update music by ID",
        request=request_serializer,
        responses={200: dict, 400: dict, 404: dict}
    )


def music_delete_swagger():
    return extend_schema(
        tags=["Music"],
        summary="Delete music",
        description="Delete music by ID",
        responses={204: None, 404: dict}
    )
