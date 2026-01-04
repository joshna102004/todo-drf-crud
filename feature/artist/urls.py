from django.urls import path
from . import controllers

urlpatterns = [
    path('artists/', controllers.list_artists, name='list_artists'),
    path('artists/<int:artist_id>/', controllers.get_artist, name='get_artist'),
    path('artists/create/', controllers.create_artist, name='create_artist'),
    path('artists/<int:artist_id>/update/', controllers.update_artist, name='update_artist'),
    path('artists/<int:artist_id>/delete/', controllers.delete_artist, name='delete_artist'),
]
