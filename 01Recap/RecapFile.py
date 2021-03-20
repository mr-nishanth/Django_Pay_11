

# Avoid file loaction Hotcoding (Setting.py)

# print(__file__)
# to print file name
# C:\DjangoPay\01Recap\RecapFile.py (In Windows)

# import os
# print(os.path.abspath(__file__))
# to print absolute location/path
# C:\DjangoPay\01Recap\RecapFile.py (In Windows)

# print(os.path.dirname(os.path.abspath(__file__)))
# to print directory location/path
# C:\DjangoPay\01Recap
# return without filename only directory

'''
# models.py related stuff's
class Employee():
    def __init__(self,name,id):
        self.empName = name
        self.empID = id

        # String Representation
    def __str__(self):
        return f" Name: {self.empName} and ID {self.empID}"

    def __repr__(self):
        return f" Name: {self.empName} and ID {self.empID}"

emp1 = Employee('Karthir', 100)
print(emp1)

'''