from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Hotel, Room
# Create your views here.


def index(request):
    return render(request, "reservation/index.html")

def hotel_list(request):
    room_list = Room.objects.all()
    print("hello", room_list)
    return render(request, "reservation/index.html", {"room_list": room_list})
