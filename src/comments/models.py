from src.movies.models import Movie
from django.db import models
from django.db.models.deletion import CASCADE
from src.users.models import User


class Comments(models.Model):
    content = models.CharField(max_length=500, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=CASCADE)
    movie = models.ForeignKey(Movie, on_delete=CASCADE, related_name="body")
