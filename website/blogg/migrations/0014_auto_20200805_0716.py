# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-05 07:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0013_auto_20200805_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 7, 16, 30, 210522, tzinfo=utc)),
        ),
    ]