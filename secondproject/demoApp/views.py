from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def gm_view(request):
    return HttpResponse(content='<h1>GOOD MORNING</h1>')

def ga_view(request):
    return HttpResponse(content='<h1>GOOD AFTERNOON</h1>')

def ge_view(request):
    return HttpResponse(content='<h1>GOOD EVENING</h1>')

def gn_view(request):
    return HttpResponse(content='<h1>GOOD NIGHT</h1>')
