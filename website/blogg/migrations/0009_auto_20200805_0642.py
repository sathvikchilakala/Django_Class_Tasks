# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-05 06:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0008_auto_20200805_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 6, 42, 50, 403218, tzinfo=utc)),
        ),
    ]