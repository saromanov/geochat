from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from .models import Message
longitude = -53.124
latitude = -18.004
user_location = Point(longitude, latitude, srid=4326)

class IndexView(generic.ListView):
    template_name = 'messages/index.html'
    context_object_name = 'near_messages'
    model = Message
    paginate_by=10

    def get_queryset(self):
        """Return nearest messages
        http://127.0.0.1:8000/messages?d=200&lat=-18.004&lon=-53.124
        """
        distance_m = self.request.GET.get('d')
        lat = self.request.GET.get('lat')
        lon = self.request.GET.get('lon')
        print(lon, lat)
        return Message.objects.annotate(distance=Distance('geometry', make_point(lon, lat))).filter(distance__lt=distance_m)


def make_point(lon, lat):
    return Point(float(lon), float(lat), srid=4326)