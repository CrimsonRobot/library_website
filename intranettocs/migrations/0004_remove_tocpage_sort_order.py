# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranettocs', '0003_auto_20160328_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tocpage',
            name='sort_order',
        ),
    ]
