from django.contrib import admin
from .models import Reservation, Hotel, Room 


admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)

