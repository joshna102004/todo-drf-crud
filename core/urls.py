# core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Music APIs
    path('music/', include('feature.music.urls')),

    # Artist APIs ✅ ADD THIS
    path('artist/', include('feature.artist.urls')),

    # Todo APIs
    path('api/todo/', include('feature.todo.urls')),
]
