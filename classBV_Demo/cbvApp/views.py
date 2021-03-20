from django.shortcuts import render

# Create your views here.

# form --> forms.ModelForm
# Model --> models.Model

# view --> View

from django.views.generic import View

from django.http import HttpResponse

class FirstView(View):
    #  get->instance function
    def get(self, request):
        return HttpResponse("<i>Hello Everone</i>")


# for Templates
from django.views.generic import TemplateView
class SecondView(TemplateView):
    template_name = 'cbvApp/base.html'