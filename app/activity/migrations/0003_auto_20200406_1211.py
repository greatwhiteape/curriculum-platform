# Generated by Django 3.0.5 on 2020-04-06 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20200406_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activitytagrelationship',
            old_name='lesson',
            new_name='activity',
        ),
    ]
