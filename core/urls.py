# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


path('api/', include('core.feature.todo.urls')),
# All todo URLs prefixed with /api/
]
