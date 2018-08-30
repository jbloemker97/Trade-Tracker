# Generated by Django 2.1 on 2018-08-30 06:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_auto_20180828_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='shares',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 8, 30, 6, 13, 52, 474975)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 8, 30, 6, 13, 52, 474975)),
        ),
    ]
