# core/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('music/', include('feature.music.urls')),
    path('api/todo/', include('feature.todo.urls')),
]
