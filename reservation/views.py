from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Hotel, Room
# Create your views here.


def index(request):
    room_list = Room.objects.all()
    return render(request, "reservation/index.html", {"room_list": room_list})

def hotels(request):
    hotels = Hotel.objects.all()
    return render(request, 'reservation/hotels.html', {'hotels': hotels})

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'reservation/rooms.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'reservation/room_detail.html', {'room': room})

def search_room(request):
    if request.method == "POST":
        location_query = request.GET.get("location", "")

        # Perform the search based on the location query
        rooms = Room.objects.filter(hotel__location__icontains=location_query)

        context = {
            "rooms": rooms,
            "search_query": location_query,
        }
        return render(request, "reservation/room_results.html", context)
    return render(request, "reservation/index.html")