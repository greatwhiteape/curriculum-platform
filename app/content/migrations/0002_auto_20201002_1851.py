# Generated by Django 3.0.10 on 2020-10-02 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='image_alt',
            field=models.CharField(blank=True, help_text='Alt tag for image', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='searchpage',
            name='image_alt',
            field=models.CharField(blank=True, help_text='Alt tag for image', max_length=100, null=True),
        ),
    ]
