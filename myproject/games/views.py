from rest_framework import generics
from .models import Game
from .serializers import GameSerializer

# Create your views here.
class GameListAPIView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameCreateAPIView(generics.CreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer