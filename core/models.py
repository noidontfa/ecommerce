from django.db import models
from django.urls import reverse
BADGE_CHOICES = [
    ('New','New'),
    ('Bestseller','Bestseller'),



]

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=20)
    naming = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    badge = models.CharField(choices=BADGE_CHOICES,max_length=10, blank=True, null= True)
    slug = models.CharField(max_length=20) # slug url

    #image
    def __str__(self):
        return f'{self.naming}'


    def display_price(self):
        return '{}'.format(self.price if self.price != round(self.price) else int(self.price))     


    def get_slug_url(self):
        return reverse('core:product-detail', kwargs={
            'slug': self.slug
        })