# Generated by Django 2.1.1 on 2018-09-10 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea1', '0007_auto_20180908_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(),
        ),
    ]