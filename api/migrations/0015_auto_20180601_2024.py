# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-01 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20180601_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apiheader',
            old_name='name',
            new_name='key',
        ),
    ]
