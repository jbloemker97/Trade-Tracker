# Generated by Django 2.1 on 2018-09-30 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0017_auto_20180930_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 30, 15, 53, 34, 651030)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 9, 30, 15, 53, 34, 651030)),
        ),
    ]
