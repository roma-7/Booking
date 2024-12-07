from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import RegisterView, HotelViewSet, RoomViewSet, ReviewViewSet, BookingViewSet, CustomLoginView
from .views import LogoutView

router = SimpleRouter()
router.register(r'hotels', HotelViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reviews', ReviewViewSet)
router.register('booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
