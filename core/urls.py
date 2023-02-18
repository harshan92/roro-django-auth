from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshToken

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshToken.as_view()),
]