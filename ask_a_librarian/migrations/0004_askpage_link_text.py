# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-09 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_a_librarian', '0003_auto_20160307_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='askpage',
            name='link_text',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
