from django.core.exceptions import ValidationError
from feature.music.model.models import Music
from .dataclasses import MusicData

def _to_dict(music: Music):
    return {
        "id": music.id,
        "title": music.title,
        "artist": music.artist,
        "duration": music.duration,
        "created_at": music.created_at,
    }

def list_music():
    return list(Music.objects.all().order_by("-created_at").values(
        "id", "title", "artist", "duration", "created_at"
    ))

def get_music(music_id: int):
    try:
        return _to_dict(Music.objects.get(id=music_id))
    except Music.DoesNotExist:
        return None

def create_music(data: MusicData):
    try:
        music = Music.create_music(data)
        return _to_dict(music)
    except ValidationError as e:
        return {"error": str(e)}

def update_music(music_id: int, data: MusicData):
    try:
        music = Music.objects.get(id=music_id)
        updated = music.update_music(data)
        return _to_dict(updated)
    except Music.DoesNotExist:
        return None
    except ValidationError as e:
        return {"error": str(e)}

def delete_music(music_id: int):
    try:
        music = Music.objects.get(id=music_id)
        music.delete_music()
        return True
    except Music.DoesNotExist:
        return False
