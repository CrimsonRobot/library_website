# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-14 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0003_unitpage_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitpage',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Please enter the phone number using the format 773-123-4567', max_length=255),
        ),
    ]
