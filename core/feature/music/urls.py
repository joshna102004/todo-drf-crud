from django.urls import path
from .controllers import MusicController

urlpatterns = [
    path("create/", MusicController.create),
    path("", MusicController.list),
    path("get/", MusicController.get_one),
    path("update/", MusicController.update),
    path("delete/", MusicController.delete),
]
