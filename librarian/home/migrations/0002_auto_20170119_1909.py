# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 13:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='book_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 19, 9, 5, 292804)),
        ),
    ]
