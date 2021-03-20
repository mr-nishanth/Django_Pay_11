from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def one(request):
    return HttpResponse(content='<h1>One</h1>')
def two(request):
    return HttpResponse(content='<h1>Two</h1>')
def three(request):
    return HttpResponse(content='<h1>Three</h1>')
def four(request):
    return HttpResponse(content='<h1>Four</h1>')
def five(request):
    return HttpResponse(content='<h1>Five</h1>')
