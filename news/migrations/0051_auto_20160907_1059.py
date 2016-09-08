# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0050_auto_20160907_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsemailaddition',
            name='extra_text',
            field=wagtail.wagtailcore.fields.RichTextField(help_text='Text to include in emails. This can include internal or external links.'),
        ),
        migrations.AlterField(
            model_name='newsemailaddition',
            name='include_in_email_dated',
            field=models.DateField(blank=True, help_text='Emails are send automatically via cron. Only email additions with the appropriate date it will attach it to messages.', null=True),
        ),
        migrations.AlterField(
            model_name='newsemailaddition',
            name='name',
            field=models.CharField(help_text='Give this snippet of text a name to help stay organized. This name will not appear in emails.', max_length=255),
        ),
    ]
