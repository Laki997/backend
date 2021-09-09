from src.users.views import UserView
from rest_framework.routers import SimpleRouter

users_router = SimpleRouter()
users_router.register(r'users', UserView, basename='users')
