from rest_framework import viewsets, generics
from .models import Profile, Hotel, Room, Review
from .serializers import UserSerializer, HotelSerializer, RoomSerializer, ReviewSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        hotel = Hotel.objects.get(id=self.request.data['hotel'])
        if hotel.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этого отеля.")
        serializer.save()

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        hotel = Hotel.objects.get(id=self.request.data['hotel'])
        serializer.save(user=self.request.user)