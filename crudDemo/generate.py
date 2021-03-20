# Project folder la one file Create pannaporoim
# manage.py file irrukara class la
# filename generate.py

import os

# 1st setting file enga inu sollauim
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudDemo.settings')

import django

django.setup()

from crudApp.models import *
from faker import Faker
from random import *

faker = Faker()

def populate(n):
    for i in range(n):
        fsno = randint(1, 99)
        fsname = faker.name()
        fsclass = randint(1,12)
        fsaddress = faker.city()
        stud_record = Student.objects.get_or_create(sno=fsno,sname=fsname,sclass=fsclass,saddress=fsaddress)


populate(10)