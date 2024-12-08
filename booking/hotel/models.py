from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner'),
        ('admin', 'admin'),
    )

    date_registered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.ForeignKey(Profile, related_name='hotels', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Room(models.Model):
    STATUS_CHOICES = [
        ('доступно', 'доступно'),
        ('забронировано', 'забронировано'),
        ('занят', 'занят'),
    ]
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.IntegerField(choices=[(i, str(i)) for i in range(1, 31)])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='доступно')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room_number} - {self.status}"


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='hotel_reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='user_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг', blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hotel.name},{self.user.username}"


class Booking(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_bookings')
    start_date = models.DateField()
    end_date = models.DateField()
