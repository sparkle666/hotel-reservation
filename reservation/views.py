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
    
    location_query = request.GET.get("location")
    print(request.GET)
    rooms = Room.objects.filter(hotel__location__icontains=location_query)
    # rooms = Room.objects.all()
    print(rooms)
    return HttpResponse(rooms)

    # Perform the search based on the location query
    # print("Location:", location_query)
    
    # print(rooms)
        
    # return render(request, "reservation/room_results.html", {
    #     "rooms": rooms,
    #     "search_query": location_query,
    # })