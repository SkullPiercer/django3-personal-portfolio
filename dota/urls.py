from django.urls import path
from . import views

app_name = 'dota'

urlpatterns = [
    path('', views.dota, name='dota'),
]
