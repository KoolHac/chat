from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Chat(models.Model):
    name = models.CharField(max_length=800)
    def __str__(self):
        return self.name

class Message(models.Model):
    title = models.CharField(max_length=5000, default=None)
    sender = models.CharField(max_length=800, default=None)
    room = models.ForeignKey(Chat, on_delete=models.CASCADE, default=None)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title
   