# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-23 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_apigroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.ApiGroup'),
            preserve_default=False,
        ),
    ]