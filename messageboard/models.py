from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.user_name


class Message(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')
    user_name = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

