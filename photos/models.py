from django.db import models
from django.db.models import CharField, TextField


# Create your models here.


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> CharField:
        return self.name


class Photo(models.Model):
    objects = None
    image = models.ImageField(null=True, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()

    def __str__(self) -> TextField:
        return self.description
