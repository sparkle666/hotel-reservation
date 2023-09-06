from django.urls import path
from .views import index, hotel_list

urlpatterns = [
    path('', hotel_list, name = "index")
]
