# Generated by Django 2.1 on 2018-09-11 06:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0005_auto_20180911_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='trades',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trades.Trades'),
        ),
        migrations.AlterField(
            model_name='trades',
            name='entry_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 9, 11, 6, 13, 34, 871254)),
        ),
        migrations.AlterField(
            model_name='trades',
            name='exit_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2018, 9, 11, 6, 13, 34, 871254)),
        ),
    ]
