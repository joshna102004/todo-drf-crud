from django.db import models
from django.core.exceptions import ValidationError
from feature.music.dataclasses import MusicData

class Music(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # ---------- MODEL VALIDATION ----------
    @staticmethod
    def validate_data(data: MusicData):
        if not data.title:
            raise ValidationError("Title is required")
        if len(data.title) > 200:
            raise ValidationError("Title too long")
        if not data.artist:
            raise ValidationError("Artist is required")
        if data.duration <= 0:
            raise ValidationError("Duration must be positive")

    # ---------- CREATE ----------
    @classmethod
    def create_music(cls, data: MusicData):
        cls.validate_data(data)
        return cls.objects.create(
            title=data.title,
            artist=data.artist,
            duration=data.duration
        )

    # ---------- UPDATE ----------
    def update_music(self, data: MusicData):
        self.validate_data(data)
        self.title = data.title
        self.artist = data.artist
        self.duration = data.duration
        self.save()
        return self

    # ---------- DELETE ----------
    def delete_music(self):
        self.delete()