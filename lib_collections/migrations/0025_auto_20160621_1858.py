# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0024_auto_20160616_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectingareapage',
            name='display_hours_in_right_sidebar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='collectionpage',
            name='display_hours_in_right_sidebar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='display_hours_in_right_sidebar',
            field=models.BooleanField(default=False),
        ),
    ]
