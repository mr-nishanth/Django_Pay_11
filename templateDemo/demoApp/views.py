from django.shortcuts import render

# Create your views here.
import datetime
def display(request):
    message = 'Hai, '
    date = datetime.datetime.now()
    usrName = "Vasee"

    hour = int(date.strftime('%H'))
    if hour < 12:
        message += "Good Morning"
    if hour < 4:
        message += "Good Afternoon"
    else:
        message += "Good Evening"

    date_dict = {'display_date': date , 'name':usrName,'greeting':message}
    return render(request,'demoApp/base.html',context=date_dict)

