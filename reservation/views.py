from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Hotel, Room
from .forms import SearchRoomForm
# Create your views here.


def index(request):
    # Check if the book form was submited redirect to the room results page for booking
    if request.method == "POST":
        print("Request is a post")
        form = SearchRoomForm(request.POST)
        
        if form.is_valid():
            location = form.cleaned_data["location"]
            check_in = form.cleaned_data["check_in"]
            check_out = form.cleaned_data["check_out"]
            
            print(location, check_in, check_out)
            
            rooms = Room.objects.filter(hotel__location__icontains=location)
            
            return render(request, "reservation/room_results.html", {"rooms": rooms})
        
    # Else if a get, get all available rooms from db and display to the index page  
    room_list = Room.objects.all()
    form = SearchRoomForm()
    
    return render(request, "reservation/index.html", {"room_list": room_list, "form": form})

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
    
    form = SearchRoomForm(request.GET)
    
    if form.is_valid():
        print("Form is valid...")
        print(form)
        return redirect("/")
    # location_query = request.GET.get("location")
    # print(request.GET)
    # rooms = Room.objects.filter(hotel__location__icontains=location_query)
    # # rooms = Room.objects.all()
    # print(rooms)
    form = SearchRoomForm()
    room_list = Room.objects.all()
    return render(request, "reservation/room_results.html", {"room_list": room_list, "form": form})

    # Perform the search based on the location query
    # print("Location:", location_query)
    
    # print(rooms)
        
    # return render(request, "reservation/room_results.html", {
    #     "rooms": rooms,
    #     "search_query": location_query,
    # })