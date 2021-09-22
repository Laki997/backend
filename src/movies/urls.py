from .views import MovieViewSet, ElasticViewSet
from rest_framework import routers


movie_router = routers.SimpleRouter()
movie_router.register(r'movies', MovieViewSet, basename='movies')

elastic_router = routers.SimpleRouter()
elastic_router.register(r'elastic', ElasticViewSet, basename='elastic')