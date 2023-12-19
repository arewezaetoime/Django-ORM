import os
import django
from django.db.models import QuerySet

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


# Create queries within functions
def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(
        name=name,
        species=species,
    )

    return f"{pet.name} is a very cute {pet.species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


def show_all_locations() -> str:
    locations_ord_by_desc = Location.objects.all().order_by('-id')
    # print(locations_ord_by_desc)
    return '\n'.join(str(loc) for loc in locations_ord_by_desc)

# print(show_all_locations())


def new_capital() -> None:
    new_location = Location.objects.first()
    new_location.is_capital = True
    new_location.save()


def get_capitals() -> str:
    return Location.objects.all().filter(is_capital=True).values('name')


def delete_first_location() -> None:
    Location.objects.first().delete()


def apply_discount() -> None:
    for car in Car.objects.all():
        percentage_off = sum(int(x) for x in str(car.year)) / 100
        discount = float(car.price) * percentage_off
        car.price_with_discount = float(car.price) - discount
        car.save()

# apply_discount()


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car() -> None:
    Car.objects.last().delete()


def show_unfinished_tasks():
    list_unfinished_tasks = []
    for task in Task.objects.filter(is_finished=False):
        list_unfinished_tasks.append(f'Task - {task.title} needs to be done until {task.due_date}!')

    return '\n'.join(list_unfinished_tasks)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(x) - 3) for x in text)
    matching_titles = Task.objects.filter(title=task_title)

    for task in matching_titles:
        task.description = decoded_text
        task.save()


def get_deluxe_rooms() -> str:
    deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    output = []

    if deluxe_rooms:
        for room in deluxe_rooms:
            if room.id % 2 != 1:
                output.append(str(room))

        return '\n'.join(output)


def increase_room_capacity() -> None:

    all_rooms = HotelRoom.objects.all().order_by('id')
    previous_room_capacity = None

    for room in all_rooms:

        if not room.is_reserved:
            continue

        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity = room.id

        previous_room_capacity = room.capacity
        room.save()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    if first_room:
        first_room.is_reserved = True
        first_room.save()


def delete_last_room() -> None:
    last_room = HotelRoom.objects.last()

    if last_room.is_reserved:
        last_room.delete()
