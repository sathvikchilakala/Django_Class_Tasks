# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-05 05:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0007_auto_20200805_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 5, 2, 55, 122646, tzinfo=utc)),
        ),
    ]