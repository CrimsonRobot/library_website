# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-14 16:13
from __future__ import unicode_literals

import base.models
from django.db import migrations
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('intranetunits', '0058_auto_20160930_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intranetunitspage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(help_text='Photographer, artist, or creator of image', required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(help_text='Details about or description of image', required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to image source (needed for Creative Commons)', required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Link to a larger version of the image', required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Secondary'), ('btn-reserve', 'Reservation')], default='btn-primary')), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StructBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', icon='title', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), help_text='A talk or event with a title, presenter             room number, and description', icon='edit', label=' '))), icon='date', template='base/blocks/agenda.html')), ('clear', wagtail.wagtailcore.blocks.StructBlock(())), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right + click in a table cell for more options. Use <em>text</em> for italics, <strong>text</strong> for bold, and <a href="https://duckduckgo.com">text</a> for links.', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'language': 'en', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'}, template='base/blocks/table.html')), ('staff_listing', wagtail.wagtailcore.blocks.StructBlock((('staff_listing', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), help_text='Be sure to select staff pages from Loop.', icon='edit', label='Staff listing')), ('show_photos', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show staff photographs.', required=False)), ('show_contact_info', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show contact information.', required=False)), ('show_subject_specialties', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show subject specialties.', required=False))), icon='group', template='base/blocks/staff_listing.html')), ('solo_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='Single image with caption on the right')), ('duo_image', wagtail.wagtailcore.blocks.StructBlock((('image_one', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='First of two images displayed             side by side')), ('image_two', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='Second of two images displayed             side by side'))), help_text='Two images stacked side by side'))), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='intranetunitspage',
            name='intro',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(help_text='Photographer, artist, or creator of image', required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(help_text='Details about or description of image', required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.URLBlock(help_text='Link to image source (needed for Creative Commons)', required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Link to a larger version of the image', required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Secondary'), ('btn-reserve', 'Reservation')], default='btn-primary')), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StructBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(icon='time', required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', icon='title', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False)))), help_text='A talk or event with a title, presenter             room number, and description', icon='edit', label=' '))), icon='date', template='base/blocks/agenda.html')), ('clear', wagtail.wagtailcore.blocks.StructBlock(())), ('table', wagtail.contrib.table_block.blocks.TableBlock(help_text='Right + click in a table cell for more options. Use <em>text</em> for italics, <strong>text</strong> for bold, and <a href="https://duckduckgo.com">text</a> for links.', table_options={'autoColumnSize': False, 'colHeaders': False, 'contextMenu': True, 'editor': 'text', 'height': 108, 'language': 'en', 'minSpareRows': 0, 'renderer': 'html', 'rowHeaders': False, 'startCols': 3, 'startRows': 3, 'stretchH': 'all'}, template='base/blocks/table.html')), ('staff_listing', wagtail.wagtailcore.blocks.StructBlock((('staff_listing', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.PageChooserBlock(), help_text='Be sure to select staff pages from Loop.', icon='edit', label='Staff listing')), ('show_photos', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show staff photographs.', required=False)), ('show_contact_info', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show contact information.', required=False)), ('show_subject_specialties', wagtail.wagtailcore.blocks.BooleanBlock(default=False, help_text='Show subject specialties.', required=False))), icon='group', template='base/blocks/staff_listing.html')), ('solo_image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='Single image with caption on the right')), ('duo_image', wagtail.wagtailcore.blocks.StructBlock((('image_one', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='First of two images displayed             side by side')), ('image_two', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('citation', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True)), ('caption', wagtail.wagtailcore.blocks.RichTextBlock(blank=True, null=True, required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(help_text='Invisible text for screen readers', required=False))), help_text='Second of two images displayed             side by side'))), help_text='Two images stacked side by side'))), blank=True),
        ),
    ]
