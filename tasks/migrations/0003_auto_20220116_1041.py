# Generated by Django 3.2.6 on 2022-01-16 03:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='note',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='task',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 3, 41, 46, 788278)),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 3, 41, 46, 788278)),
        ),
    ]
