from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.get_user_by_id, name='get_user_by_id'),
]