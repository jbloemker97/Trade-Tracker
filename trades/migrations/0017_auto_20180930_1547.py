# Generated by Django 2.1 on 2018-09-30 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0016_auto_20180930_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 30, 15, 47, 53, 236073)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 9, 30, 15, 47, 53, 237073)),
        ),
    ]