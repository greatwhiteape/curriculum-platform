# Generated by Django 3.0.8 on 2020-08-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_asset_live'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
