from rest_framework import generics
from .models import Game
from .serializers import GameSerializer

# Create your views here.
class GameListCreateView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    operation_id = 'game_list_create'

class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    operation_id = 'game_detail'