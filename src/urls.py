from django.urls import include, path
from rest_framework.routers import DefaultRouter
from src.users.urls import users_router


router = DefaultRouter()
router.registry.extend(users_router.registry)

urlpatterns = [
    path('api/', include(router.urls))
]
