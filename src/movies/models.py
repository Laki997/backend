
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import Field
from .constants import GENRE_CHOICES
from src.users.models import User


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
  
    def likes(self):
        return self.reactions.filter(reaction=True).count()
    
    def dislikes(self):
        return self.reactions.filter(reaction=False).count()


class MovieReaction(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, related_name='reactions', on_delete=CASCADE)
    reaction = models.BooleanField(null=True)

    class Meta:
        unique_together = ('user', 'movie')
