from django.contrib.gis.db import models
from django.utils import timezone
from django_cryptography.fields import encrypt

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    text = encrypt(models.TextField(max_length=1000))
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    user_id = models.IntegerField()
    #mpoly = models.MultiPolygonField()
    geometry = models.PointField()

worldborders_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'geom' : 'MULTIPOLYGON',
}

