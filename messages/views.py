from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

longitude = 13.191788
latitude = 27.761681
user_location = Point(longitude, latitude, srid=4326)

class IndexView(generic.ListView):
    template_name = 'messages/index.html'
    context_object_name = 'near_messages'
    model = Message

    def get_queryset(self):
        """Return the last five published questions."""
        return Message.objects.annotate(distance=Distance('location', user_location).order_by('distance')[0:5])

