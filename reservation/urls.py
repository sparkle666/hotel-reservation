from django.urls import path
from .views import index, reserve_room, hotels, rooms

urlpatterns = [
    path('', index, name = "index"),
    path('room/reserve/<int:room_id>/', reserve_room, name='room_detail'),
    path('hotel/', hotels, name='hotels'),
    path('room/', rooms, name='rooms'),
]
