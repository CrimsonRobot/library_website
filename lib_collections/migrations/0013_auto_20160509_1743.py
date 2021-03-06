# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtaildocs', '0007_merge'),
        ('lib_collections', '0012_auto_20160509_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exhibitpageexhibitchecklist',
            name='exhibit_checklist',
        ),
        migrations.RemoveField(
            model_name='exhibitpageexhibitchecklist',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='exhibitpageexhibitchecklist',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='exhibitpageexhibittext',
            name='exhibit_text',
        ),
        migrations.RemoveField(
            model_name='exhibitpageexhibittext',
            name='link_document',
        ),
        migrations.RemoveField(
            model_name='exhibitpageexhibittext',
            name='link_page',
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='exhibit_checklist_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='exhibit_checklist_link_external',
            field=models.URLField(blank=True, verbose_name='Exhibit checklist external link'),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='exhibit_checklist_link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='exhibit_text_document',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='exhibit_text_link_external',
            field=models.URLField(blank=True, verbose_name='Exhibit text external link'),
        ),
        migrations.AddField(
            model_name='exhibitpage',
            name='exhibit_text_link_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.DeleteModel(
            name='ExhibitPageExhibitChecklist',
        ),
        migrations.DeleteModel(
            name='ExhibitPageExhibitText',
        ),
    ]
