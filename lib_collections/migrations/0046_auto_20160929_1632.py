# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 21:32
from __future__ import unicode_literals

import base.models
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('units', '0051_auto_20160610_1600'),
        ('staff', '0038_auto_20160929_1632'),
        ('lib_collections', '0045_auto_20160926_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitChildPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_sidebar_from_here', models.BooleanField(default=False)),
                ('show_sidebar', models.BooleanField(default=False)),
                ('last_reviewed', models.DateField(blank=True, null=True, verbose_name='Last Reviewed')),
                ('quicklinks', wagtail.wagtailcore.fields.RichTextField(blank=True)),
                ('quicklinks_title', models.CharField(blank=True, max_length=100)),
                ('view_more_link', models.URLField(blank=True, default='', max_length=255)),
                ('view_more_link_label', models.CharField(blank=True, max_length=100)),
                ('change_to_callout', models.BooleanField(default=False)),
                ('display_hours_in_right_sidebar', models.BooleanField(default=False)),
                ('enable_index', models.BooleanField(default=False)),
                ('display_hierarchical_listing', models.BooleanField(default=False)),
                ('events_feed_url', models.URLField(blank=True, help_text='Link to a Tiny Tiny RSS Feed')),
                ('banner_title', models.CharField(blank=True, max_length=100)),
                ('banner_subtitle', models.CharField(blank=True, max_length=100)),
                ('news_feed_url', models.URLField(blank=True, help_text='Link to a wordpress feed from the Library News Site')),
                ('external_news_page', models.URLField(blank=True, help_text='Link to an external news page, e.g. wordpress')),
                ('rich_text_heading', models.CharField(blank=True, max_length=25)),
                ('rich_text', wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Should be a bulleted list or combination of h3 elements and bulleted lists')),
                ('rich_text_external_link', models.URLField(blank=True, help_text='Optional external link that displays next to the heading')),
                ('rich_text_link_text', models.CharField(blank=True, help_text='Display text for the rich text link', max_length=25)),
                ('body', wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(help_text='Photographer, artist, or creator of image', required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(help_text='Details about or description of image', required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to image source (needed for Creative Commons)', required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Link to a larger version of the image', required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Secondary'), ('btn-reserve', 'Reservation')], default='btn-primary')), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StructBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', icon='title', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), help_text='A talk or event with a title, presenter             room number, and description', icon='edit', label=' '))), icon='date', template='base/blocks/agenda.html')), ('clear', wagtail.wagtailcore.blocks.StructBlock(())), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right + click in a table cell for more options. Use <em>text</em> for italics, <strong>text</strong> for bold, and <a href="https://duckduckgo.com">text</a> for links.', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'language': 'en', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'}, template='base/blocks/table.html')), ('staff_listing', wagtail.wagtailcore.blocks.StructBlock((('staff_listing', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), help_text='Be sure to select staff pages from Loop.', icon='edit', label='Staff listing')), ('show_photos', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show staff photographs.', required=False)), ('show_contact_info', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show contact information.', required=False)), ('show_subject_specialties', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show subject specialties.', required=False))), icon='group', template='base/blocks/staff_listing.html')), ('solo_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='Single image with caption on the right'))), blank=True)),
                ('banner_feature', models.ForeignKey(blank=True, help_text='Banner feature images should be approximately 500 × 500 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('banner_image', models.ForeignKey(blank=True, help_text='Banners should be approximately 1200 × 200 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('content_specialist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitchildpage_content_specialist', to='staff.StaffPage')),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitchildpage_editor', to='staff.StaffPage')),
                ('internal_news_page', models.ForeignKey(blank=True, help_text='Link to an internal news page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('page_maintainer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitchildpage_maintainer', to='staff.StaffPage')),
                ('rich_text_link', models.ForeignKey(blank=True, help_text='Optional link that displays next to the heading', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lib_collections_exhibitchildpage_related', to='units.UnitPage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.AlterField(
            model_name='collectionpage',
            name='full_description',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(help_text='Photographer, artist, or creator of image', required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(help_text='Details about or description of image', required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to image source (needed for Creative Commons)', required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Link to a larger version of the image', required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Secondary'), ('btn-reserve', 'Reservation')], default='btn-primary')), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StructBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', icon='title', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), help_text='A talk or event with a title, presenter             room number, and description', icon='edit', label=' '))), icon='date', template='base/blocks/agenda.html')), ('clear', wagtail.wagtailcore.blocks.StructBlock(())), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right + click in a table cell for more options. Use <em>text</em> for italics, <strong>text</strong> for bold, and <a href="https://duckduckgo.com">text</a> for links.', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'language': 'en', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'}, template='base/blocks/table.html')), ('staff_listing', wagtail.wagtailcore.blocks.StructBlock((('staff_listing', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), help_text='Be sure to select staff pages from Loop.', icon='edit', label='Staff listing')), ('show_photos', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show staff photographs.', required=False)), ('show_contact_info', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show contact information.', required=False)), ('show_subject_specialties', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show subject specialties.', required=False))), icon='group', template='base/blocks/staff_listing.html')), ('solo_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='Single image with caption on the right'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exhibitpage',
            name='full_description',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(help_text='Photographer, artist, or creator of image', required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(help_text='Details about or description of image', required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to image source (needed for Creative Commons)', required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Link to a larger version of the image', required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Secondary'), ('btn-reserve', 'Reservation')], default='btn-primary')), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StructBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', icon='title', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), help_text='A talk or event with a title, presenter             room number, and description', icon='edit', label=' '))), icon='date', template='base/blocks/agenda.html')), ('clear', wagtail.wagtailcore.blocks.StructBlock(())), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right + click in a table cell for more options. Use <em>text</em> for italics, <strong>text</strong> for bold, and <a href="https://duckduckgo.com">text</a> for links.', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'language': 'en', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'}, template='base/blocks/table.html')), ('staff_listing', wagtail.wagtailcore.blocks.StructBlock((('staff_listing', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), help_text='Be sure to select staff pages from Loop.', icon='edit', label='Staff listing')), ('show_photos', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show staff photographs.', required=False)), ('show_contact_info', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show contact information.', required=False)), ('show_subject_specialties', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show subject specialties.', required=False))), icon='group', template='base/blocks/staff_listing.html')), ('solo_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='Single image with caption on the right'))), blank=True, null=True),
        ),
    ]
