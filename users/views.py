from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.shortcuts import get_object_or_404
def index(req):
    return HttpResponse("Geo chat test")

def get_user_by_id(request, id):
    p = get_object_or_404(Person, id=id)
    return HttpResponse("This user have username: {0}".format(p.username))
