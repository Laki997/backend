from django.urls import path
from .views import RegistrationApiView

urlpatterns = [
    path('auth/register', RegistrationApiView.as_view())
]
