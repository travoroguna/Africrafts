from django.db import models
from  customer.models import User


# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
