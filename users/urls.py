from django.urls import path
from . import views
from django.conf.urls import url,include

urlpatterns = [
     path('', views.PersonDetailView.as_view(),name='message-list'),
     url(r'^accounts/', include('django.contrib.auth.urls')),
]