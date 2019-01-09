from django.contrib.gis.db import models

class Message(models.Model):
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')

