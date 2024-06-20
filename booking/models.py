from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Room(models.Model):
    ROOM_TYPES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
    ]
    image = models.ImageField(upload_to='room_images/') 
    
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room}"
    