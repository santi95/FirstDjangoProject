# Generated by Django 2.1.1 on 2018-09-08 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]