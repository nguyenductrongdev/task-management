# Generated by Django 3.2.6 on 2022-01-16 12:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 12, 25, 24, 252364, tzinfo=utc)),
        ),
    ]
