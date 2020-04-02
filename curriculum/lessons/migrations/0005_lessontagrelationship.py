# Generated by Django 3.0.4 on 2020-04-02 20:50

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0002_auto_20200402_1821'),
        ('lessons', '0004_auto_20200402_2045'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonTagRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_tag_relationship', to='lessons.Lesson')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Tag')),
            ],
        ),
    ]
