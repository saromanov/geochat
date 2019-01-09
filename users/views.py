from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
def index(req):
    return HttpResponse("Geo chat test")

def get_user_by_id(request, id):
    p = Person.objects.get(id=id)
    return HttpResponse("This user have username: {0}".format(p.username))
