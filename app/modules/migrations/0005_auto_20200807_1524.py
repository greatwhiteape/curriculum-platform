# Generated by Django 3.0.8 on 2020-08-07 15:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0004_module_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='learning_outcomes',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Learning Outcomes (displays on Detail tab)'),
        ),
        migrations.AlterField(
            model_name='module',
            name='students_desc',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('copy', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('asset', wagtail.snippets.blocks.SnippetChooserBlock('assets.Asset')), ('activity', wagtail.snippets.blocks.SnippetChooserBlock('activity.Activity')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('youtube', wagtail.core.blocks.StructBlock([('youtube_video', wagtail.core.blocks.CharBlock(help_text='YouTube Video ID (https://youtu.be/XXX-XXX the XXX-XXX section)', required=True))])), ('google_doc', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text='Link to Google Doc', required=True))])), ('codap', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text='Link to CODAP', required=True))]))], blank=True, null=True, verbose_name='Resources for Students'),
        ),
        migrations.AlterField(
            model_name='module',
            name='teachers_desc',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('copy', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('asset', wagtail.snippets.blocks.SnippetChooserBlock('assets.Asset')), ('activity', wagtail.snippets.blocks.SnippetChooserBlock('activity.Activity')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('youtube', wagtail.core.blocks.StructBlock([('youtube_video', wagtail.core.blocks.CharBlock(help_text='YouTube Video ID (https://youtu.be/XXX-XXX the XXX-XXX section)', required=True))])), ('google_doc', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text='Link to Google Doc', required=True))])), ('codap', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text='Link to CODAP', required=True))]))], blank=True, null=True, verbose_name='Lessons Tab Content'),
        ),
    ]
