from django.db import models


class Base(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    description = models.TextField(null=True, blank=True)

    visible = models.BooleanField(default=True)
    like = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
        ordering = ['-updated_at']
