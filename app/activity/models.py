from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.api import APIField

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from streams import blocks

from taxonomy.serializers import (
    ProgramSerializer,
    TimeEstimateSerializer,
    AudienceSerializer,
    StandardsSerializer,
    TopicSerializer,
    TagSerializer,
    ActivityTypeSerializer,
)
@register_snippet
class Activity(ClusterableModel):
    class Meta:
        managed = True
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    # teachers_guide = models.URLField()
    overview_copy = RichTextField(null=True, blank=True)
    student_copy = RichTextField(null=True, blank=True)
    teachers_desc = StreamField(
        [
            ('title', blocks.TitleBlock()),
            ('copy', wagtail_blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('asset', SnippetChooserBlock('assets.Asset')),
            ('activity', SnippetChooserBlock('activity.Activity')),
            ('document', DocumentChooserBlock()),
            ('embed', EmbedBlock()),
            ('external', blocks.Link()),
            ('google_doc', blocks.GoogleDocEmbed()),
            ('codap', blocks.CODAPEmbed()),
            ('raw_html', wagtail_blocks.RawHTMLBlock()),
        ],
        null=True,
        blank=True
    )
    students_desc = StreamField(
        [
            ('title', blocks.TitleBlock()),
            ('copy', wagtail_blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('asset', SnippetChooserBlock('assets.Asset')),
            ('activity', SnippetChooserBlock('activity.Activity')),
            ('document', DocumentChooserBlock()),
            ('embed', EmbedBlock()),
            ('external', blocks.Link()),
            ('google_doc', blocks.GoogleDocEmbed()),
            ('codap', blocks.CODAPEmbed()),
            ('raw_html', wagtail_blocks.RawHTMLBlock()),
        ],
        null=True,
        blank=True
    )

    program = models.ForeignKey(
        'taxonomy.Program',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    time_estimate = models.ForeignKey(
        'taxonomy.TimeEstimate',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    audience = models.ForeignKey(
        'taxonomy.Audience',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    topic = models.ForeignKey(
        'taxonomy.Topic',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    activity_type = models.ForeignKey(
        'taxonomy.ActivityType',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )

    @property
    def tags(self):
        tags = [
            n.tag for n in self.tag_relationship.all()
        ]
        return tags

    # tag = models.ManyToManyField(
    #     'taxonomy.Tag',
    #     blank=True
    # )

    def __str__(self):
        return self.title


    panels = [
        FieldPanel("title"),
        # FieldPanel("teachers_guide"),
        FieldPanel("overview_copy"),
        StreamFieldPanel('teachers_desc'),
        StreamFieldPanel('students_desc'),
        SnippetChooserPanel("program"),
        InlinePanel('audience_relationship', label="Audience"),
        InlinePanel('standards_relationship', label="Standards Alignment"),
        InlinePanel('topic_relationship', label="Topics"),
        InlinePanel('tag_relationship', label="Tags"),
        # SnippetChooserPanel("tag"),
        # InlinePanel('tag_relationship', label="Tags"),
    ]

    api_fields = [
        APIField('title'),
        APIField('overview_copy'),
        APIField('teachers_desc'),
        APIField('students_desc'),
        APIField('program', serializer=ProgramSerializer()),
        APIField('audience_relationship'),
        APIField('standards_relationship'),
        APIField('topic_relationship'),
        APIField('tag_relationship'),
    ]

class ActivityTagRelationship(models.Model):
    activity = ParentalKey(
        'Activity',
        related_name='tag_relationship'
    )
    tag = models.ForeignKey(
        'taxonomy.Tag',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel('tag')
    ]

    api_fields = [
        APIField('tag', serializer=TagSerializer())
    ]

class ActivityAudienceRelationship(models.Model):
    activity = ParentalKey(
        'Activity',
        related_name='audience_relationship'
    )
    audience = models.ForeignKey(
        'taxonomy.Audience',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel('audience')
    ]

    api_fields = [
        APIField('audience', serializer=AudienceSerializer())
    ]

class ActivityStandardsRelationship(models.Model):
    activity = ParentalKey(
        'Activity',
        related_name='standards_relationship'
    )
    standard = models.ForeignKey(
        'taxonomy.Standard',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    panels = [
        FieldPanel('standard')
    ]

    api_fields = [
        APIField('standard', serializer=StandardsSerializer())
    ]

class ActivityTopicRelationship(models.Model):
    activity = ParentalKey(
        'Activity',
        related_name='topic_relationship'
    )
    topic = models.ForeignKey(
        'taxonomy.Topic',
        models.SET_NULL,
        related_name='+',
        null=True,
    )

    panels = [
        FieldPanel('topic')
    ]

    api_fields = [
        APIField('topic', serializer=TopicSerializer())
    ]
