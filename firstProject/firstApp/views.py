from django.shortcuts import render

# Create your views here.

'''
HTTPRequest : http:/localhost:8000/welcome
HTTPResponse : Displaying images or anything

Views is Bussiness logic
'''

from django.http import HttpResponse

def wish(request):
    message = "<h1> Hai Buddy How Are you </h1>"
    return HttpResponse(message)