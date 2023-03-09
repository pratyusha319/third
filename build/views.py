from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sand(request):
    return HttpResponse('sand is main important component in costruction of a building')

def bricks(request):
    return HttpResponse('bricks is main important component')

def cement(request):
    return HttpResponse('cement is main important components')