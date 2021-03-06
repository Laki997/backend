
from django.db import connections, models
from django.db.models.deletion import CASCADE
from django.db.models.enums import TextChoices
from django.db.models.fields import Field, PositiveBigIntegerField, related
from .constants import GENRE_CHOICES
from src.users.models import User
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections
# connections.create_connection(hosts=['0.0.0.0'])


class Movie(models.Model):
    class MoviesGenre(TextChoices):
        DRAMA = GENRE_CHOICES.get('DRAMA')
        COMEDY = GENRE_CHOICES.get('COMEDY')
        SF = GENRE_CHOICES.get('SF')
        HOROR = GENRE_CHOICES.get('HOROR')

    title = models.CharField(max_length=255, unique=True)
    cover_image = models.URLField(max_length=200, )
    description = models.CharField(max_length=255,)
    view_count = models.PositiveBigIntegerField(default=0)
    genre = models.CharField(max_length=20,
                             choices=MoviesGenre.choices,
                             default=MoviesGenre.DRAMA)
    @property
    def likes(self):
        return self.reactions.filter(reaction=True).count()
    @property
    def dislikes(self):
        return self.reactions.filter(reaction=False).count()

    @property
    def isWatched(self):
        return self.watch


class MovieReaction(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, related_name='reactions', on_delete=CASCADE)
    reaction = models.BooleanField(null=True)

    class Meta:
        unique_together = ('user', 'movie')


class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, related_name="watch", on_delete=CASCADE)
    watched = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'movie')
