from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Hotel, Reservation, Room
from .forms import ReserveRoomModelForm, SearchRoomForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
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
            # Make a reservation object with the current user
            reservation = Reservation(
                user=request.user, check_in=check_in, check_out=check_out)
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


def reserve_room(request, room_id):

    room = get_object_or_404(Room, id=room_id)
    print(room)
    if request.method == "POST":
        print("inside post")
        user = request.user
        form = ReserveRoomModelForm(request.POST)

        print(form)

        if form.is_valid():
            print("Form is valid")

            print(form.cleaned_data["adults"])
            print(form.cleaned_data["children"])

            reservation = form.save(commit=False)
            reservation.user = user
            reservation.room = room
            reservation.save()

            return render(request, 'reservation/reservations.html', {'reservation': reservation})
    form = ReserveRoomModelForm()
    return render(request, 'reservation/room_detail.html', {'room': room, "form": form})


@login_required  # Requires user authentication
def user_reservation_list(request):
    # Filter reservations for the current user and where check-in is today or in the future
    reservations = Reservation.objects.filter(user=request.user)

    return render(request, 'reservation/reservations.html', {'reservations': reservations})
