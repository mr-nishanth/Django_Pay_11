from django.shortcuts import render ,redirect

# Create your views here.
from django.http import HttpResponse

def welcomepage(request):
    return HttpResponse("<i>This is Welcome Page</i>")

def homepage(request):
    return render(request,'crudApp/base.html')

#

from crudApp.models import Student
def retrieve_view(request):
    student = Student.objects.all()
    stus_obj = {'stu_info': student}
    return render(request,'crudApp/retrieve.html',context=stus_obj)

#

from crudApp.forms import StudentForm
def create_view(request):
    form = StudentForm()

    # Now the form is adding in DB
    # form ===> DB
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/retrieve')
    return render(request,'crudApp/create.html',context={'form':form})



def delete_view(request, id):
    # id is primary key
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('/crudApp/retrieve')

'''
# Delete + Create = Update
'''
def update_view(request ,id):

    student = Student.objects.get(id=id)
    if request.method == "POST":

        form = StudentForm(request.POST,instance=student) #Important

        if form.is_valid():
            form.save()
            return redirect('/retrieve')

    return render(request , 'crudApp/update.html',context={'student':student})
