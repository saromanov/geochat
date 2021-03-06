from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from .models import Person
from django.contrib.auth.mixins import LoginRequiredMixin

class PersonDetailView(DetailView):
    template_name = 'users/user.html'
    model = Person

class LoginView(LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
