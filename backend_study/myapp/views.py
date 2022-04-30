from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    return HttpResponse('<h1>Random</h1>'+str(random.random()))

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read'+id)