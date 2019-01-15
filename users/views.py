from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Person

class PersonDetailView(DetailView):

    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
