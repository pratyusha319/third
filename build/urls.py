from build.views import *

from django.urls import path
 
app_name='something'

urlpatterns=[
    path('sand/',sand,name='sand'),
    path('bricks/',bricks,name='bricks'),
    path('cement/',cement,name='cement'),
]