from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='users')

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('accounts:view_profil')
