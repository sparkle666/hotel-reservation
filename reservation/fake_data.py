import os
import random
from faker import Faker
from django.utils import timezone
from django.core.files import File
from .models import Hotel, Room, Reservation  # Replace 'yourapp' with your actual app name

fake = Faker()

# Create hotels
def create_hotels(num_hotels):
    hotels = []
    for _ in range(num_hotels):
        hotel = Hotel.objects.create(
            name=fake.company(),
            location=fake.address(),
            created=timezone.now()
        )
        hotels.append(hotel)
    return hotels

# Create rooms for each hotel
def create_rooms(hotels, num_rooms_per_hotel):
    for hotel in hotels:
        for _ in range(num_rooms_per_hotel):
            room = Room.objects.create(
                room_type=random.choice([choice[0] for choice in ROOM_TYPES]),
                amenities=AMENITIES,
                price=random.uniform(50, 500),
                isOccupied=random.choice([True, False]),
                created=timezone.now(),
                description=fake.paragraph(),
                hotel=hotel,
            )

            # Add a random image to the room (requires image files in a directory)
            image_path = 'path/to/your/image.jpg'  # Replace with a valid image path
            if os.path.isfile(image_path):
                with open(image_path, 'rb') as image_file:
                    room.featured_image.save(os.path.basename(image_path), File(image_file))

# Create reservations
def create_reservations(num_reservations, rooms):
    for _ in range(num_reservations):
        user = User.objects.create(username=fake.user_name())
        room = random.choice(rooms)
        check_in = fake.date_time_between(start_date='-30d', end_date='+30d')
        check_out = check_in + timezone.timedelta(days=random.randint(1, 7))
        reservation = Reservation.objects.create(
            user=user,
            room=room,
            check_in=check_in,
            check_out=check_out,
        )

# if __name__ == '__main__':
#     num_hotels = 5  # Change as needed
#     num_rooms_per_hotel = 10  # Change as needed
#     num_reservations = 20  # Change as needed

#     hotels = create_hotels(num_hotels)
#     create_rooms(hotels, num_rooms_per_hotel)
#     rooms = Room.objects.all()
#     create_reservations(num_reservations, rooms)
