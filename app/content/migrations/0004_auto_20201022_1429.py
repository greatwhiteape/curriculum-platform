# Generated by Django 3.0.10 on 2020-10-22 14:29

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20201022_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='featured_copy',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Copy describing the program & the featured curricula', null=True, verbose_name='Introductory Content Copy'),
        ),
        migrations.AlterField(
            model_name='contentpage',
            name='featured_title',
            field=models.CharField(blank=True, help_text='Title for intro copy (optional)', max_length=100, null=True, verbose_name='Introduction Title'),
        ),
        migrations.AlterField(
            model_name='searchpage',
            name='featured_copy',
            field=wagtail.core.fields.RichTextField(blank=True, help_text='Copy describing the program & the featured curricula', null=True, verbose_name='Introductory Content Copy'),
        ),
        migrations.AlterField(
            model_name='searchpage',
            name='featured_title',
            field=models.CharField(blank=True, help_text='Title for intro copy (optional)', max_length=100, null=True, verbose_name='Introduction Title'),
        ),
    ]
