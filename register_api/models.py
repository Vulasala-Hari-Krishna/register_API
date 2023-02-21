from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=255)
    work = models.ManyToManyField('Work')

    def __str__(self):
        return self.name

class Work(models.Model):
    LINK_CHOICES = (
        ('Y', 'Youtube'),
        ('I', 'Instagram'),
        ('O', 'Other')
    )
    link = models.CharField(max_length=255)
    work_type = models.CharField(max_length=1, choices=LINK_CHOICES)

    def __str__(self):
        return self.link
