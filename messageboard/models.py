from django.db import models
from django.contrib.auth import authenticate

class Message(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=30)

    def __str__(self):
        return self.title
