# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-31 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0055_auto_20161014_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conferencepage',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='conferencepage',
            name='tagline',
        ),
    ]
