# Generated by Django 2.1.5 on 2021-06-30 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210630_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 30, 12, 47, 47, 3759), verbose_name='date published'),
        ),
    ]
