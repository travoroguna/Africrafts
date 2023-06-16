from django.db import models
from customer.models import User
from artisan.models import Artisan
# from accounts.models import Customer
from artisan.models import Product
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
# class Customer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class OrderProduct(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name

    def get_total_item_price(self):
        return self.product.price * self.quantity


class ShippingAddress(models.Model):
    address = models.CharField(max_length=200, null=False, blank=True)
    city = models.CharField(max_length=200, null=False, blank=True)
    state = models.CharField(max_length=200, null=False, blank=True)
    zip_code = models.CharField(max_length=200, null=False, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    ordered = models.BooleanField(default=False)
    shipping_address = models.ForeignKey('ShippingAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.customer}'s order. is ordered: {self.ordered}"

    @property
    def get_total(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.get_total_item_price()
        return total

    @property
    def get_total_quantity(self):
        total = 0
        for order_product in self.products.all():
            total += order_product.quantity
        return total
