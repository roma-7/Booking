from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, HotelViewSet, RoomViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include(router.urls)),
]