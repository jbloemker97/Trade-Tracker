# Generated by Django 2.1 on 2018-08-27 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0003_auto_20180827_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 8, 27, 19, 28, 31, 87915)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_comments',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 8, 27, 19, 28, 31, 87915)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='trades',
            name='pnl',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
