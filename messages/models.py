from django.contrib.gis.db import models

class Message(models.Model):
    text = models.TextField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    lon = models.FloatField()
    lat = models.FloatField()
    area = models.IntegerField()
    user_id = models.IntegerField()
    mpoly = models.MultiPolygonField()
    geometry = models.PointField()

    def __str__(self):
        return self.text

