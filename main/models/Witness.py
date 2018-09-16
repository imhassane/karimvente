from django.db import models


class Witness(models.Model):

    content = models.TextField()
    author = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='witness/')

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author
    
    class Meta:
        ordering = ['-created_at']
