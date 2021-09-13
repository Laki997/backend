from django.urls import include, path
from rest_framework.routers import DefaultRouter
from src.users.urls import users_router
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)


router = DefaultRouter()
router.registry.extend(users_router.registry)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/token', TokenRefreshView.as_view())
]
