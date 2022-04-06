from django.db import models
from .utils import create_skus

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="products", blank=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("products:detail", kwargs={"pk":self.pk})


class SKU(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="products",
        on_delete=models.CASCADE,
    )
    serial_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.serial_number)



class Generation(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="generations",
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)

    def save(self, *args, **kwargs):
        quantity = self.quantity

        if quantity > 0:
            create_skus(self.product, self.quantity)

        super().save(*args, **kwargs)