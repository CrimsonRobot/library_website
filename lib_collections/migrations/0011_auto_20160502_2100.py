# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-02 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0010_auto_20160502_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpagesubjectplacement',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_pages', to='subjects.Subject'),
        ),
    ]
