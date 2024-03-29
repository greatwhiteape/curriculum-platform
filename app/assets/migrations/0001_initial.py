# Generated by Django 3.0.6 on 2020-05-28 21:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('asset_link', wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()), ('external', wagtail.core.blocks.StructBlock([('link_text', wagtail.core.blocks.CharBlock(default='Asset can be accessed here.', max_length=50)), ('url', wagtail.core.blocks.URLBlock(help_text='Link to external resource', required=True))])), ('google_doc', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text='Link to Google Doc', required=True))])), ('codap', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock(help_text='Link to CODAP', required=True))])), ('embed', wagtail.embeds.blocks.EmbedBlock()), ('raw_html', wagtail.core.blocks.RawHTMLBlock())], blank=True, null=True)),
                ('student_asset', models.BooleanField(null=True)),
                ('student_intro', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='Copy for the Student Page')),
                ('asset_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='taxonomy.AssetType')),
                ('program', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='taxonomy.Program')),
                ('time_estimate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.TimeEstimate')),
            ],
            options={
                'verbose_name': 'Curriculum Asset',
                'verbose_name_plural': 'Curriculum Assets',
            },
        ),
        migrations.CreateModel(
            name='AssetTopicRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='topic_relationship', to='assets.Asset')),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='taxonomy.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='AssetTagRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag_relationship', to='assets.Asset')),
                ('tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='AssetStandardsRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='standards_relationship', to='assets.Asset')),
                ('standard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Standard')),
            ],
        ),
        migrations.CreateModel(
            name='AssetAudienceRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audience', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taxonomy.Audience')),
                ('module', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='audience_relationship', to='assets.Asset')),
            ],
        ),
    ]
