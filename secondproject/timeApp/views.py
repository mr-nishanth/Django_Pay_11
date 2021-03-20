from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import datetime
def tellMeTime(request):
    time = datetime.datetime.now()
    result ='<h1>Hai The time is : ' +str(object=time) + '</h1>'
    return HttpResponse(content=result)