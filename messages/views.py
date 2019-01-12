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
        """Return nearest messages"""
        return Message.objects.annotate(distance=Distance('geometry', user_location)).filter(distance__lt=500)

