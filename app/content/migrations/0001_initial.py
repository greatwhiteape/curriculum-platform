# Generated by Django 3.0.6 on 2020-05-28 21:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxonomy', '0001_initial'),
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero_text', models.CharField(blank=True, help_text='Marketing-speak about GRMI EDU (100 Characters Max)', max_length=100, null=True)),
                ('featured_title', models.CharField(blank=True, help_text='Section title', max_length=100, null=True)),
                ('featured_copy', models.TextField(blank=True, help_text='Featured content copy', null=True)),
                ('search_tag', models.TextField(blank=True, help_text='<app-root> tag plus modifiers like Program or modulesOnly', null=True)),
                ('image', models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Program')),
            ],
            options={
                'verbose_name': 'Search',
                'verbose_name_plural': 'Search Pages',
                'managed': True,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('hero_text', models.CharField(blank=True, help_text='Marketing-speak about GRMI EDU (100 Characters Max)', max_length=100, null=True)),
                ('featured_title', models.CharField(blank=True, help_text='Section title', max_length=100, null=True)),
                ('featured_copy', models.TextField(blank=True, help_text='Featured content copy', null=True)),
                ('body', wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('copy', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('asset', wagtail.snippets.blocks.SnippetChooserBlock('assets.Asset')), ('activity', wagtail.snippets.blocks.SnippetChooserBlock('activity.Activity')), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True, null=True)),
                ('image', models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Program')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content Pages',
                'managed': True,
            },
            bases=('wagtailcore.page',),
        ),
    ]
