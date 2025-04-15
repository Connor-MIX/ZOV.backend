from django.urls import path
from .views import GameListAPIView, GameDetailAPIView, GameCreateAPIView

urlpatterns = [
    path('', GameListAPIView.as_view(), name='game-list'),
    path('create/', GameCreateAPIView.as_view(), name='game-create'),
    path('<int:pk>/', GameDetailAPIView.as_view(), name='game-detail'),
]