# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirbrowse', '0017_dirbrowsepage_rich_text_external_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='dirbrowsepage',
            name='change_to_callout',
            field=models.BooleanField(default=False),
        ),
    ]
