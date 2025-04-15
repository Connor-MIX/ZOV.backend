from django.urls import path
from .views import GameListCreateView, GameDetailView

urlpatterns = [
    path('', GameListCreateView.as_view(), name='game-list-create'),
    path('<int:pk>/', GameDetailView.as_view(), name='game-detail'),
]