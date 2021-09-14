
from .views import MovieViewSet
from rest_framework import routers

movie_router = routers.SimpleRouter()
movie_router.register(r'movies', MovieViewSet, basename='movies')