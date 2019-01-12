# Generated by Django 2.1.5 on 2019-01-12 16:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('messages.one', '0005_auto_20190112_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='area',
        ),
        migrations.RemoveField(
            model_name='message',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='lon',
        ),
        migrations.AlterField(
            model_name='message',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 12, 16, 35, 43, 742809, tzinfo=utc), verbose_name='date published'),
        ),
    ]
