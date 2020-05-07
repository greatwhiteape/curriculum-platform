# Generated by Django 3.0.6 on 2020-05-07 20:07

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_lesson_lesson_download'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='intro_copy',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Header Intro'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='student_intro',
            field=wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Student Page Intro'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='students_desc',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('copy', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('asset', wagtail.snippets.blocks.SnippetChooserBlock('assets.Asset')), ('activity', wagtail.snippets.blocks.SnippetChooserBlock('activity.Activity')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True, null=True, verbose_name='Student Page Content'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teachers_desc',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('copy', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('asset', wagtail.snippets.blocks.SnippetChooserBlock('assets.Asset')), ('activity', wagtail.snippets.blocks.SnippetChooserBlock('activity.Activity')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True, null=True, verbose_name='Overview Tab Content'),
        ),
    ]
