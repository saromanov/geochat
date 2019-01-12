from decimal import Decimal
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import GEOSGeometry 

from .models import Message
longitude = Decimal(-18.0048)
latitude = Decimal(-53.124389)
user_location = GEOSGeometry("POINT({0} {1})".format(longitude, latitude))

class IndexView(generic.ListView):
    template_name = 'messages/index.html'
    context_object_name = 'near_messages'
    model = Message

    def get_queryset(self):
        """Return nearest messages"""
        print(Message.objects.filter(
            point__distance_lte=(user_location, Distance(km=10))
        ))
        return Message.objects.annotate(distance=Distance('geometry', user_location)).order_by('distance')[0:5]

