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
)

@register_snippet
class Lesson(ClusterableModel):
    template = 'lessons/lesson_page.html'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    title = models.CharField(max_length=100)
    subtitle = models.CharField(
        max_length=300,
        null=True,
        blank=True,
    )
    intro_copy = RichTextField(
        verbose_name="Header Intro",
        null=True,
        blank=True
    )
    overview_copy = RichTextField(
        verbose_name="Overview Tab Copy",
        null=True,
        blank=True
    )
    student_intro = RichTextField(
        verbose_name="Student Page Intro",
        null=True,
        blank=True
    )
    teachers_guide = models.URLField(
        null=True,
        blank=True
    )
    lesson_download = models.URLField(
        null=True,
        blank=True
    )
    learning_outcomes = RichTextField(
        null=True,
        blank=True
    )
    teachers_desc = StreamField(
        [
            ('title', blocks.TitleBlock()),
            ('copy', wagtail_blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('asset', SnippetChooserBlock('assets.Asset')),
            ('activity', SnippetChooserBlock('activity.Activity')),
            ('document', DocumentChooserBlock()),
            ('embed', EmbedBlock()),
        ],
        null=True,
        blank=True,
        verbose_name="Overview Tab Content",
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
        ],
        null=True,
        blank=True,
        verbose_name="Student Page Content",
    )

    @property
    def standards_alignment(self):
        standards_alignment = [
            n.standard for n in self.standards_relationship.all()
        ]
        return standards_alignment

    time_estimate = models.ForeignKey(
        'taxonomy.TimeEstimate',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )

    program = models.ForeignKey(
        'taxonomy.Program',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    @property
    def audience(self):
        audience = [
            n.audience for n in self.audience_relationship.all()
        ]
        return audience

    @property
    def tags(self):
        tags = [
            n.tag for n in self.tag_relationship.all()
        ]
        return tags

    panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('subtitle'),
            FieldPanel('intro_copy'),
            ImageChooserPanel('hero_image'),
        ], heading="Header Section"),
        MultiFieldPanel([
            FieldPanel('overview_copy'),
            FieldPanel('student_intro'),
            FieldPanel('learning_outcomes'),
            FieldPanel('teachers_guide'),
            FieldPanel('lesson_download'),
        ], heading="Intro Content"),
        MultiFieldPanel([
            StreamFieldPanel('teachers_desc'),
            StreamFieldPanel('students_desc'),
        ], heading="Tabbed Content"),
        MultiFieldPanel([
            SnippetChooserPanel('program'),
            SnippetChooserPanel('time_estimate'),
            InlinePanel('audience_relationship', label="Audience"),
            InlinePanel('standards_relationship', label="Standards Alignment"),
            InlinePanel('topic_relationship', label="Topics"),
            InlinePanel('tag_relationship', label="Tags"),
        ], heading="Lesson Metadata")
    ]

    api_fields = [
        APIField('title'),
        APIField('subtitle'),
        APIField('hero_image'),
        APIField('intro_copy'),
        APIField('student_intro'),
        APIField('learning_outcomes'),
        APIField('teachers_guide'),
        APIField('teachers_desc'),
        APIField('students_desc'),
        APIField('program', serializer=ProgramSerializer()),
        APIField('time_estimate', serializer=TimeEstimateSerializer()),
        APIField('audience_relationship'),
        APIField('standards_relationship'),
        APIField('topic_relationship'),
        APIField('tag_relationship'),
    ]

    def __str__(self):
        return self.title
class LessonTagRelationship(models.Model):
    lesson = ParentalKey(
        'Lesson',
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

class LessonAudienceRelationship(models.Model):
    lesson = ParentalKey(
        'Lesson',
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

class LessonStandardsRelationship(models.Model):
    lesson = ParentalKey(
        'Lesson',
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

class LessonTopicRelationship(models.Model):
    lesson = ParentalKey(
        'Lesson',
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
