from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from .models import Message
longitude = -18.0048
latitude = -53.124389
user_location = Point(longitude, latitude, srid=4326)

class IndexView(generic.ListView):
    template_name = 'messages/index.html'
    context_object_name = 'near_messages'
    model = Message

    def get_queryset(self):
        """Return the last five published questions."""
        return Message.objects.annotate(distance=Distance('geometry', user_location)).order_by('distance')[0:5]

