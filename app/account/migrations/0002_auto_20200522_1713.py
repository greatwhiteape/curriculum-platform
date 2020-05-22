# Generated by Django 3.0.6 on 2020-05-22 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gmri_uuid',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='has_cas_connection',
            field=models.BooleanField(default=False),
        ),
    ]
