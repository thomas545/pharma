from django.utils.crypto import get_random_string


RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789"


def create_skus(product, quantity):
    from .models import SKU

    new_quantity = quantity
    skus = []

    for _ in range(0, new_quantity):
        skus.append(
            SKU(
                product=product, serial_number=get_random_string(8, RANDOM_STRING_CHARS)
            )
        )
        new_quantity -= 1

    SKU.objects.bulk_create(skus)
