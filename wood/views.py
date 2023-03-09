from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cupboards(request):
    return HttpResponse('cupboards is one of thing in construction')
def doors(request):
    return HttpResponse('wood is one of thing in construction')
