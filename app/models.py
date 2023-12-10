from django.db import models
from django.core.cache import cache

class Character(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_occupation_display(self):
        return self.occupation

    class Meta:
        ordering = ['name']
