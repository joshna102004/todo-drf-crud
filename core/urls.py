# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Todo APIs
    path('api/todo/', include('core.feature.todo.urls')),

    # Music APIs
    path('api/music/', include('core.feature.music.urls')),
    path("api/music/", include("core.feature.music.urls")),
]
