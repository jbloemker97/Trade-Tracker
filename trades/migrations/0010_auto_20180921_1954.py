# Generated by Django 2.1 on 2018-09-21 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0009_auto_20180921_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 21, 19, 54, 54, 189502)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 9, 21, 19, 54, 54, 189502)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='success',
            field=models.CharField(max_length=10),
        ),
    ]
