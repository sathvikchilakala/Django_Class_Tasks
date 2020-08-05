# Generated by Django 3.0.7 on 2020-07-12 02:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0003_auto_20200707_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnqDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mail', models.CharField(max_length=30)),
                ('mno', models.IntegerField()),
                ('message', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 2, 17, 46, 220088, tzinfo=utc)),
        ),
    ]
