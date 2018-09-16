from django.db import models
from .Product import Product


class Picture(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField(upload_to='products')

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.product.name
