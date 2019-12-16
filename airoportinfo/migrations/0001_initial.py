# Generated by Django 2.2.7 on 2019-11-23 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.AutoField(primary_key=True, serialize=False)),
                ('departureDate', models.DateField()),
                ('depatureTime', models.TimeField()),
                ('departureFrom', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('arrivalDate', models.DateField()),
                ('arrivalTime', models.TimeField()),
                ('gate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
