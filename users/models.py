from django.db import models
from django import forms
from django.contrib.auth.models import User

class User(models.Model):
    bio = models.TextField(max_length=500, blank=True)
    username = models.TextField(max_length=50)

