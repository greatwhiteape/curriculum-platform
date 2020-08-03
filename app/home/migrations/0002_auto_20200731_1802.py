# Generated by Django 3.0.8 on 2020-07-31 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='labventure_section_button_link',
            field=models.URLField(blank=True, help_text='Link that call to button action links to', null=True, verbose_name='LabVenture Button Link'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='labventure_section_button_text',
            field=models.CharField(blank=True, help_text='Text for call to action button (25 Characters Max).', max_length=25, null=True, verbose_name='LabVenture Call to Action Button Text'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='labventure_section_copy',
            field=models.TextField(blank=True, help_text='Marketing copy for the Labventure.', max_length=255, null=True, verbose_name='LabVenture Section Copy'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='labventure_section_hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='LabVenture Section Hero Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='labventure_section_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='LabVenture Section Logo'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='labventure_section_title',
            field=models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255, null=True, verbose_name='LabVenture Section Title'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vitalsigns_section_button_link',
            field=models.URLField(blank=True, help_text='Link that call to button action links to', null=True, verbose_name='Citizen Science Button Link'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vitalsigns_section_button_text',
            field=models.CharField(blank=True, help_text='Text for call to action button (25 Characters Max).', max_length=25, null=True, verbose_name='Citizen Science Call to Action Button Text'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vitalsigns_section_copy',
            field=models.TextField(blank=True, help_text='Marketing copy for the Vital Signs.', null=True, verbose_name='Citizen Science Copy'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vitalsigns_section_hero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Citizen Science Hero Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vitalsigns_section_logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Citizen Science Logo'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='vitalsigns_section_title',
            field=models.CharField(blank=True, help_text='Title to display above the promo copy', max_length=255, null=True, verbose_name='Citizen Science Section Title'),
        ),
    ]
