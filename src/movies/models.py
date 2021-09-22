
from django.db import connections, models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.enums import TextChoices
from django.db.models.fields import Field, PositiveBigIntegerField, related
from .constants import GENRE_CHOICES
from src.users.models import User
from easy_thumbnails import fields


class Image(models.Model):
    image = fields.ThumbnailerImageField(upload_to='full-size/', resize_source=dict(size=(400, 400)))
    thumbnail = fields.ThumbnailerImageField(upload_to='thumbnails/', resize_source=dict(size=(200,200)))


class Movie(models.Model):
    class MoviesGenre(TextChoices):
        DRAMA = GENRE_CHOICES.get('DRAMA')
        COMEDY = GENRE_CHOICES.get('COMEDY')
        SF = GENRE_CHOICES.get('SF')
        HOROR = GENRE_CHOICES.get('HOROR')

    title = models.CharField(max_length=255, unique=True)
    cover_image = models.OneToOneField(Image, on_delete=RESTRICT)
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
