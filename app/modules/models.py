from __future__ import unicode_literals

from django.db import models

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.search import index

from streams import blocks
class Module(ClusterableModel):
    template = 'modules/module_page.html'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
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
    intro_copy = models.TextField(
        verbose_name="Marketing Copy",
        null=True,
        blank=True
    )
    student_intro = models.TextField(
        verbose_name="Copy for the Student Page",
        null=True,
        blank=True
    )
    teachers_guide = models.URLField(
        null=True,
        blank=True
    )
    learning_outcomes = models.TextField(
        null=True,
        blank=True
    )
    lessons_desc = StreamField([
        ("title", blocks.TitleBlock()),
    ], null=True, blank=True)
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
        on_delete = models.SET_NULL
    )
        
    @property
    def standards_alignment(self):
        standards_alignment = [
            n.standard for n in self.module_standards_relationship.all()
        ]
        return standards_alignment
    
    @property
    def audience(self):
        audience = [
            n.audience for n in self.module_audience_relationship.all()
        ]
        return audience
    
    @property
    def tags(self):
        tags = [
            n.tag for n in self.module_tag_relationship.all()
        ]
        return tags
    
    @property
    def topics(self):
        topics = [
            n.topic for n in self.module_topic_relationship.all()
        ]
        return tags

    # audience = models.ManyToManyField(
    #     'taxonomy.Audience',
    #     blank=True
    # )
    # tag = models.ManyToManyField(
    #     'taxonomy.Tag', 
    #     blank=True
    # )
    # topic = models.ManyToManyField(
    #     'taxonomy.Topic',
    #     blank=True
    # )

    
    panels = [
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            FieldPanel('title'),
            FieldPanel('subtitle'),
        ], heading="Hero Section"),
        MultiFieldPanel([
            FieldPanel('intro_copy'),
            FieldPanel('student_intro'),
            StreamFieldPanel('lessons_desc'),
        ], heading="Marketing Speak"),
        MultiFieldPanel([
            FieldPanel('teachers_guide'),
            SnippetChooserPanel('program'),
            SnippetChooserPanel('time_estimate'),
            InlinePanel('module_audience_relationship', label="Audience"),
            InlinePanel('module_standards_relationship', label="Standards Alignment"),
            InlinePanel('module_topic_relationship', label="Topics"),
            InlinePanel('module_tag_relationship', label="Tags"),
        ], heading="Module Metadata")
    ]

class ModuleTagRelationship(models.Model):
    module = ParentalKey(
        'Module',
        related_name='module_tag_relationship'
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

class ModuleAudienceRelationship(models.Model):
    module = ParentalKey(
        'Module',
        related_name='module_audience_relationship'
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

class ModuleStandardsRelationship(models.Model):
    module = ParentalKey(
        'Module',
        related_name='module_standards_relationship'
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

class ModuleTopicRelationship(models.Model):
    module = ParentalKey(
        'Module',
        related_name='module_topic_relationship'
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