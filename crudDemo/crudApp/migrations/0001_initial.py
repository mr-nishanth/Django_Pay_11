# Generated by Django 3.1.6 on 2021-03-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=30)),
                ('sclass', models.IntegerField()),
                ('saddress', models.CharField(max_length=50)),
            ],
        ),
    ]
