# Generated by Django 2.1 on 2018-09-29 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0011_auto_20180928_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 29, 10, 47, 48, 544132)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 9, 29, 10, 47, 48, 544132)),
        ),
    ]
