# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-02 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20180601_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apibodyparam',
            name='type',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='apiresponseparam',
            name='type',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
