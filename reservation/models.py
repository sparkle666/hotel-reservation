from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


ROOM_TYPES = (
    ('ST', 'Standard'),
    ('DL', 'Deluxe'),
    ('SU', 'Suite'),
    ('FM', 'Family'),   
    ('EX', 'Executive'),
    ('BD', 'Bridal'),
    ('PR', 'Presidential'),
)

AMENITIES = {
    "bed": 2,
    "capacity": 2,
    "free wifi": True,
    "Private bathroom" : True,
    "Air conditioning": True,
    "Balcony": True,
}

RATING = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return self.name
    
class Room(models.Model):
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES, default='ST')
    amenities = models.JSONField(default=AMENITIES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isOccupied = models.BooleanField(default = False)
    featured_image = models.ImageField(upload_to = "images/", blank = True)
    created = models.DateTimeField(auto_now_add=timezone.now())
    description = models.TextField()
    rating = models.CharField(max_length = 2, choices = RATING)
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.room_number}, {self.room_type}"


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.room} - {self.check_in} to {self.check_out}"
  
