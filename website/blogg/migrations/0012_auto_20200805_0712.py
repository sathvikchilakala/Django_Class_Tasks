# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-05 07:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0011_auto_20200805_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 7, 12, 51, 806494, tzinfo=utc)),
        ),
    ]