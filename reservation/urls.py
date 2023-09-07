from django.urls import path
from .views import index, room_detail, hotels, rooms, search_room

urlpatterns = [
    path('', index, name = "index"),
    path('rooms/<int:room_id>/', room_detail, name='room_detail'),
    path('hotels/', hotels, name='hotels'),
    path('rooms/', rooms, name='rooms'),
    path('search/', search_room, name='search_room'),
]
