# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0037_auto_20160624_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferenceindexpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a WordPress Feed from the Library News Site'),
        ),
        migrations.AddField(
            model_name='conferencepage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a WordPress Feed from the Library News Site'),
        ),
        migrations.AddField(
            model_name='conferencesubpage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a WordPress Feed from the Library News Site'),
        ),
    ]
