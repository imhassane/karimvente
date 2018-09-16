from .Base import Base
from django.shortcuts import reverse
from django.db import models


class Category(Base):
    
    image = models.ImageField(upload_to="categories/", default="default.png")
    
    def get_absolute_url(self):
        return reverse('main:category', kwargs={'slug': self.slug})
