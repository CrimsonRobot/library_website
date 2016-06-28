# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirbrowse', '0012_dirbrowsepage_events_feed_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dirbrowsepage',
            name='events_feed_url',
            field=models.URLField(blank=True, help_text='Link to a Tiny Tiny RSS Feed'),
        ),
    ]