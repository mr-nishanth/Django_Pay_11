from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def display(request):
    return HttpResponse("<h1>Hello</h1>")


from . import forms
def empDetailsView(request):
    form = forms.EmployeeInfoForm()
    
    empInfo = {'form': form}
    return render(request , 'formApp/input.html' , context=empInfo)
