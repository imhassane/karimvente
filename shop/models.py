from django.db import models
from main.models import Product


# Create your models here.
class Base(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Order(Base):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Bucket(Base):

    name = models.CharField(max_length=150, default="")
    value = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    validated = models.BooleanField(default=False)
    sent = models.BooleanField(default=False)
    order = models.ManyToManyField(Order, related_name='orders')
