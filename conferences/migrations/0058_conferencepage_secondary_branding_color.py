# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-31 17:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0057_auto_20161031_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencepage',
            name='secondary_branding_color',
            field=models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator(message='Please enter a hex color, e.g. #012043', regex='^#[a-zA-Z0-9]{6}$')]),
        ),
    ]
