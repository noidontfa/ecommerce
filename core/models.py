from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
# User = get_user_model()

BADGE_CHOICES = [
    ('New','New'),
    ('Bestseller','Bestseller'),



]
class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.username

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=20)
    naming = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    badge = models.CharField(choices=BADGE_CHOICES,max_length=10, blank=True, null= True)
    slug = models.CharField(max_length=20) # slug url
    discount_price = models.FloatField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    #image
    def __str__(self):
        return f'{self.naming}'


    def display_price(self):
        return '{}'.format(self.price if self.price != round(self.price) else int(self.price))     


    def get_slug_url(self):
        return reverse('core:product-detail', kwargs={
            'slug': self.slug
        })

User = get_user_model()
class Cart(models.Model):

    product = models.ForeignKey('Product',on_delete= models.CASCADE)
    user_other = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
     
    def get_product_price(self):
        return self.product.price * self.quantity 