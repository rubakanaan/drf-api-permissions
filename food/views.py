from rest_framework import generics
from .models import Food
from .serializers import FoodSerializer
from .permissions import IsAuthorOrReadOnly

class FoodList(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    