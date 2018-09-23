from django.db import models
from .Base import Base
from .Category import Category

from django.shortcuts import reverse


class Product(Base):

    price = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)

    # Dimensions du produit
    width = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    ray = models.FloatField(default=0.0)

    # Disponibilité du produit.
    availability = models.DateField()

    # Image du produit.
    image = models.ImageField(upload_to='products', default='')

    # Catégories du produit
    category = models.ManyToManyField(Category, related_name='products')

    def get_absolute_url(self):
        return reverse('main:product', kwargs={'slug': self.slug})
