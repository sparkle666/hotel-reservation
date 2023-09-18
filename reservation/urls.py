from django.urls import path
from .views import index, reserve_room, hotels, rooms, user_reservation_list

urlpatterns = [
    path('', index, name="index"),
    path('room/reserve/<int:room_id>/', reserve_room, name='room_detail'),
    path('hotel/', hotels, name='hotels'),
    path('room/', rooms, name='rooms'),
    path('reservations/', user_reservation_list,
         name='reservations'),
]
