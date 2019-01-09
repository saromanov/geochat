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

