# Generated by Django 2.2.7 on 2019-12-15 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20191214_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='buyer',
        ),
    ]
