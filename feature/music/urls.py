from django.urls import path
from .controllers import MusicController

urlpatterns = [
    path("", MusicController.list),                     # GET all
    path("get/<int:id>/", MusicController.get_one),     # GET by id
    path("create/", MusicController.create),            # POST
    path("update/<int:id>/", MusicController.update),   # PUT/PATCH
    path("delete/<int:id>/", MusicController.delete),   # DELETE
]
