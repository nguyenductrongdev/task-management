# Generated by Django 3.2.6 on 2022-01-17 12:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 17, 12, 9, 28, 274743, tzinfo=utc)),
        ),
    ]
