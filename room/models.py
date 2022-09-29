from lib2to3.pgen2.token import SLASHEQUAL
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Room(models.Model):

    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name


class Message(models.Model):

    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('data_added',)