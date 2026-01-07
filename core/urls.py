from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version="v1",
        description="API documentation for Artist and Music services",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # ✅ Redirect root URL to Swagger
    path("", lambda request: redirect("swagger/")),

    # ✅ Admin
    path("admin/", admin.site.urls),

    # ✅ Your feature APIs
    path("api/", include("feature.urls")),

    # ✅ Swagger URLs
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="redoc"),
]
