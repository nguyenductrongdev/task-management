# Generated by Django 3.2.6 on 2022-01-16 05:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20220116_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 1, 16, 5, 1, 35, 446030, tzinfo=utc)),
        ),
    ]