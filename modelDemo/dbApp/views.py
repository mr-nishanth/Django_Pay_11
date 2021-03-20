from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    message = "<i>This is Welcome Page</i>"
    return HttpResponse(message)

#
from dbApp.models import Employee

def empDetails(request):
    emp_data = Employee.objects.all()
    emp_dict={'emp_list':emp_data}
    return render(request,'dbApp/base.html',context=emp_dict)