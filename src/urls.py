
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from src.users.urls import users_router
from src.movies.urls import movie_router, elastic_router
from src.comments.urls import comment_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)


router = DefaultRouter()
router.registry.extend(users_router.registry)
router.registry.extend(movie_router.registry)
router.registry.extend(comment_router.registry)
router.registry.extend(elastic_router.registry)


urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/token', TokenRefreshView.as_view()),
]
