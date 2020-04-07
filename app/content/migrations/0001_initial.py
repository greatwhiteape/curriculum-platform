# Generated by Django 3.0.5 on 2020-04-05 20:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
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
                ('body', wagtail.core.fields.RichTextField(blank=True, help_text='Content Body', null=True)),
                ('image', models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content Pages',
                'managed': True,
            },
            bases=('wagtailcore.page',),
        ),
    ]
