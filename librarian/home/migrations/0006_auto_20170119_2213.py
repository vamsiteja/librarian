# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 16:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20170119_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 22, 13, 47, 403738)),
        ),
    ]
