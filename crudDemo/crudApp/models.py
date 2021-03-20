from django.db import models

# Create your models here.

# now create class

class Student(models.Model):
    sno = models.IntegerField()
    sname = models.CharField(max_length=30)
    sclass = models.IntegerField()
    saddress = models.CharField(max_length=50)

    