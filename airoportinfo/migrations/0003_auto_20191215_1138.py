# Generated by Django 2.2.7 on 2019-12-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airoportinfo', '0002_news_newsimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newsImage',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
