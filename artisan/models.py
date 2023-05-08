from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Artisan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/uploads/', null=True, blank=True)

    def __str__(self):
        return f"{User.get_email(self.user)} - {self.name}"