# Generated by Django 3.0.5 on 2020-04-06 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        ('activity', '0003_auto_20200406_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='tag',
            field=models.ManyToManyField(blank=True, to='taxonomy.Tag'),
        ),
    ]
