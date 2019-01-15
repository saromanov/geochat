from django.db import models
from django import forms
from django.contrib.auth.models import User

class Person(User):
    bio = models.TextField(max_length=500, blank=True)
    tags = models.TextField(max_length=100)

    def __str__(self):
        return '{0} {1}'.format(self.firstname, self.lastname)

