from wood.views import *

from django.urls import path
 
app_name='nothing'

urlpatterns=[
    path('cupboards/',cupboards,name='cupboards'),
    path('doors/',doors,name='doors'),
]