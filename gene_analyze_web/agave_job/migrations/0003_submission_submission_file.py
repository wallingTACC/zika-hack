# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agave_job', '0002_auto_20160909_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='submission_file',
            field=models.FileField(null=True, upload_to=b''),
        ),
    ]
