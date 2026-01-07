from django.urls import path, include

urlpatterns = [
    path("artist/", include("feature.artist.urls")),
    path("music/", include("feature.music.urls")),
]
