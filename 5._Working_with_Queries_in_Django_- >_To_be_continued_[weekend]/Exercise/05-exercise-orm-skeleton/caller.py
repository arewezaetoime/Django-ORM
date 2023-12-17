import os
from typing import List

import django
from django.db.models import Case, When, Value, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import ArtworkGallery, Laptop, ChessPlayer


# Create and check models
def show_highest_rated_art() -> str:
    artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()
    return f"{artwork.art_name} is the highest-rated art with {artwork.rating} rating!"


def bulk_create_arts(first_art, second_art) -> None:
    ArtworkGallery.objects.bulk_create([
        first_art,
        second_art
    ])


def delete_negative_rated_arts() -> None:
    ArtworkGallery.objects.filter(rating__lt=0).delete()


# artwork1 = ArtworkGallery(artist_name="Vincent van Gogh", art_name="Starry Night", rating=4, price=1200000.0)
# artwork2 = ArtworkGallery(artist_name="Leonardo da Vinci", art_name="Mona Lisa", rating=5, price=1500000.0)
#
# # Bulk saves the instances
# bulk_create_arts(artwork1, artwork2)
# print(show_highest_rated_art())
# print(ArtworkGallery.objects.all())


def show_the_most_expensive_laptop() -> str:
    best_laptop = Laptop.objects.order_by('-price', 'id').first()

    return f"{best_laptop.brand} is the most expensive laptop available for {best_laptop.price}$!"


def bulk_create_laptops(*args: List[Laptop]) -> None:
    Laptop.objects.bulk_create(*args)


def update_to_512_GB_storage() -> None:
    # Laptop.objects.filter(Q(brand="Lenovo") | Q(brand="Asus")).update(storage=512)
    Laptop.objects.filter(brand__in=["Asus", "Lenovo"]).update(storage=512)


def update_to_16_GB_memory() -> None:
    Laptop.objects.filter(brand__in=["Apple", "Dell", "Acer"]).update(memory=16)


def update_operation_systems() -> None:
    Laptop.objects.update(
        operation_system=Case(
            When(brand="Asus", then=Value("Windows")),
            When(brand="Apple", then=Value("MacOS")),
            When(brand__in=["Dell", "Acer"], then=Value("Linux")),
            When(brand="Lenovo", then=Value("Chrome OS")),
            default=F('operation_system')
        )
    )

    # Laptop.objects.filter(brand="Asus").update(operation_system="Windows")
    # Laptop.objects.filter(brand="Apple").update(operation_system="MacOS")
    # Laptop.objects.filter(brand__in=["Dell", "Acer"]).update(operation_system="Linux")
    # Laptop.objects.filter(brand="Lenovo").update(operation_system="Chrome OS")


def delete_inexpensive_laptops() -> None:
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(*args: List[ChessPlayer]) -> None:
    ChessPlayer.objects.bulk_create(*args)


def delete_chess_players() -> None:
    # make it abstract, get the title from the meta fields
    ChessPlayer.objects.filter(title="no title").delete()


def change_chess_games_won() -> None:
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost() -> None:
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn() -> None:
    ChessPlayer.objects.update(games_drawn=10)


def grand_chess_title_GM() -> None:
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")


def grand_chess_title_IM() -> None:
    # ChessPlayer.objects.filter(Q(rating__gte=2300) & Q(rating_lt=2400)).update(title="IM")
    ChessPlayer.objects.filter(rating__range=[2300, 2399]).update(title="IM")


def grand_chess_title_FM() -> None:
    ChessPlayer.objects.filter(rating__range=[2200, 2299]).update(title="FM")


def grand_chess_title_regular_player() -> None:
    ChessPlayer.objects.filter(rating__range=[0, 2199]).update(title="regular player")



# Run and print your queries
