from .views import CommentsViewSet
from rest_framework import routers

comment_router = routers.SimpleRouter()
comment_router.register(r'comments', CommentsViewSet, basename='comments')