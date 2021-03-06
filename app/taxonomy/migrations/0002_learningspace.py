# Generated by Django 3.0.11 on 2020-12-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True)),
                ('learning_space', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Learning Space',
                'verbose_name_plural': 'Learning Space',
                'managed': True,
            },
        ),
    ]
