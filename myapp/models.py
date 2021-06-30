from django.db import models
from django.http import HttpResponse
from datetime import datetime

# Create your models here.
class Message(models.Model):
    message_me = models.TextField()
    message_published = models.DateTimeField("date published", default=datetime.now())

def __str__(self):
    return self.message_me