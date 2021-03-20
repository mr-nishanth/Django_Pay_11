from django.contrib import admin


# import your models here.
from dbApp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    emp_details = ['empNo', 'empName', 'empSalary', 'empAddress']

admin.site.register(Employee,EmployeeAdmin)