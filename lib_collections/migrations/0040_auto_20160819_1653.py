# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0039_auto_20160819_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectingareapage',
            name='banner_subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='collectionpage',
            name='banner_subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
