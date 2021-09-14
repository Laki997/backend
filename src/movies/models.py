from django.db import models
from django.db.models.enums import TextChoices
from .constants import GENRE_CHOICES


class Movie(models.Model):
    class MoviesGenre(TextChoices):
        DRAMA = GENRE_CHOICES.get('DRAMA')
        COMEDY = GENRE_CHOICES.get('COMEDY')
        SF = GENRE_CHOICES.get('SF')
        HOROR = GENRE_CHOICES.get('HOROR')

    title = models.CharField(max_length=255, unique=True)
    cover_image = models.URLField(max_length=200, )
    description = models.CharField(max_length=255,)
    genre = models.CharField(max_length=20,
                             choices=MoviesGenre.choices,
                             default=MoviesGenre.DRAMA)
