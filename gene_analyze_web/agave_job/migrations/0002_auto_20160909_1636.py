# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 16:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agave_job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='datetime',
            field=models.DateTimeField(default=datetime.date(2016, 1, 1)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=30.28, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submission',
            name='lng',
            field=models.DecimalField(decimal_places=3, default=-97.7, max_digits=8),
            preserve_default=False,
        ),
    ]