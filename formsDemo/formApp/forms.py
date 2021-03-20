from django import forms

# Create subClass for form parent class

class EmployeeInfoForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    salary = forms.IntegerField()
