# Generated by Django 2.1 on 2018-09-21 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0008_auto_20180917_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='success',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 21, 19, 42, 59, 159207)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 9, 21, 19, 42, 59, 159207)),
        ),
    ]
