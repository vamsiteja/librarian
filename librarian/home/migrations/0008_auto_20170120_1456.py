# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 09:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20170119_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 20, 14, 56, 22, 635877)),
        ),
    ]