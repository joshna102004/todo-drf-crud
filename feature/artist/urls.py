from django.urls import path
from .controllers import list_artists, get_artist, create_artist, update_artist, delete_artist

urlpatterns = [
    path('artists/', list_artists, name='list_artists'),
    path('artists/<int:artist_id>/', get_artist, name='get_artist'),
    path('artists/create/', create_artist, name='create_artist'),
    path('artists/<int:artist_id>/update/', update_artist, name='update_artist'),
    path('artists/<int:artist_id>/delete/', delete_artist, name='delete_artist'),
]
