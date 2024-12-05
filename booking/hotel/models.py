from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('hotel_owner', 'Hotel Owner'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    date_registered = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

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
        ('оккупировано', 'оккупировано'),
    ]
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    room_number = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Room {self.room_number} - {self.status}"



class Review(models.Model):
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.hotel.name} by {self.user.username}"