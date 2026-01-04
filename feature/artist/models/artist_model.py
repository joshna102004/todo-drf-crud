from django.db import models
from django.core.exceptions import ValidationError
from feature.artist.dataclasses.artist_dataclass import ArtistData
import datetime

CURRENT_YEAR = datetime.datetime.now().year

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50, null=True, blank=True)
    debut_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    # ---------- VALIDATIONS ----------
    def clean(self):
        if not self.name or len(self.name.strip()) < 2:
            raise ValidationError("Artist name must be at least 2 characters")

        if self.genre and len(self.genre.strip()) < 2:
            raise ValidationError("Genre must be at least 2 characters")

        if self.debut_year:
            if self.debut_year < 1900 or self.debut_year > CURRENT_YEAR:
                raise ValidationError(
                    f"Debut year must be between 1900 and {CURRENT_YEAR}"
                )

    # ---------- CREATE ----------
    @classmethod
    def create(cls, data: ArtistData):
        artist = cls(
            name=data.name.strip(),
            genre=data.genre.strip() if data.genre else None,
            debut_year=data.debut_year
        )
        artist.full_clean()
        artist.save()
        return artist

    # ---------- UPDATE ----------
    def update(self, data: ArtistData):
        self.name = data.name.strip() if data.name else self.name
        self.genre = data.genre.strip() if data.genre else self.genre
        self.debut_year = (
            data.debut_year if data.debut_year is not None else self.debut_year
        )
        self.full_clean()
        self.save()
        return self
