from django import forms

from crudApp.models import Student

class StudentForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'
        # exclude = ['sno']




# data = user <--> user
# Meta data --> Data about data
    #  eg: Mail --> Sender / IP ? / Date / Time / ISP Provider / Browser
    #  Mail is data
    # Sender / IP ? / Date / Time / ISP Provider / Browser is Meta data and  cookies is also