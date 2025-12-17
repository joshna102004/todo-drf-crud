from django.urls import path
from .controllers import (
    create_music_controller,
    list_music_controller,
    get_music_controller,
    update_music_controller,
    delete_music_controller,
)

urlpatterns = [
    path("create/", create_music_controller),
    path("list/", list_music_controller),
    path("get/", get_music_controller),
    path("update/", update_music_controller),
    path("delete/", delete_music_controller),
]
