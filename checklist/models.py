from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Checklist(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=CASCADE)
    url = models.URLField(blank=True)
    needed = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class User(models.Model):
    email = models.EmailField()
    checkedList = models.ManyToManyField(Checklist, blank=True)
