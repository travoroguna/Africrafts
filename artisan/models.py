from django.db import models
from customer.models import User
from django.utils.text import slugify 
from django.urls import reverse
from uuid import uuid4


# Create your models here.
class Artisan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)



class Product(models.Model):
    user = models.ForeignKey(Artisan, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/uploads/', null=True, blank=True)

    def __str__(self):
        return f"{User.get_email(self.user.user)} - {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name + self.description + str(uuid4()))
        super().save(*args, **kwargs)

    def get_add_to_cart_url(self):
        return reverse('add_to_cart', kwargs={'slug': self.slug})