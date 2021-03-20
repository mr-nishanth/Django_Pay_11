from django.contrib import admin

# Register your models here.

from crudApp.models import Student

class StudentAdmin(admin.ModelAdmin):
    stu_list = ['sno','sname','sclass','saddress']

admin.site.register(Student, StudentAdmin)

'''

- models.py la DB create only
- DB la irrthu data ah yaduthutu varaa (admin.ModelAdmin) etha super class la vaitchu subclass create pannauim
- models.py la ena ena field vaitchu irruthomoo , that fields vaitchu
- subclass and field ah list ah sollauim
# - ipo etha list la ena string kuduthurukomoo ethutha Student admin page display  yakuim (doubt)
# - sonnatha na DB la irruthu etha fields/column ah use panna  mudiuim

Student and StudentAdmin  connect panne register pannuim

- Namaa create pandra dbclass(Student) ikku thaneeeyaa Admin potaraa (StudentAdmin)
'''
