# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-27 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20180524_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=50)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Api')),
            ],
        ),
    ]
