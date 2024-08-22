from django.db import models
from datetime import datetime
from django.utils.timezone import now

# Create your models here.

class Room(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True
    )
    added_on = models.DateTimeField(
        default=now(),
        blank=True
    )
    
    def __str__(self):
        return f'{self.name}'
    
class Message(models.Model):
    value = models.TextField(
        null=False
    )
    created_on = models.DateTimeField(
        default=now(),
        blank=True
    )
    user = models.CharField(
        max_length=1000,
        null=False
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.created_on | self.room}'
