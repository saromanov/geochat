from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
     path('', views.PersonDetailView.as_view(),name='message-list')
]