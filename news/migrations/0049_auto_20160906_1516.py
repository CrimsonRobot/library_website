# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-06 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0048_newsemailaddition_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsemailaddition',
            old_name='name',
            new_name='title',
        ),
    ]
