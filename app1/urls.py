from django.urls import path
from app1.views import *
app_name='somethhing'
urlpatterns=[
    path('mahi/',mahi,name='mahi'),
    path('app1',app1,name='app1'),
]