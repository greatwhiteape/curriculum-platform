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
class Module(Page):
    template = 'modules/module_page.html'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
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
    lessons_desc = models.TextField(
        verbose_name = 'Friendly Description of Lessons',
        null=True,
        blank=True
    )
    standards_alignment = models.ForeignKey(
        'taxonomy.Standard',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
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
    audience = models.ForeignKey(
        'taxonomy.Audience',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    tag = models.ForeignKey(
        'taxonomy.Tag', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    topic = models.ForeignKey(
        'taxonomy.Topic',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('hero_image'),
            # FieldPanel('title'), 
            FieldPanel('subtitle')
        ], heading="Hero Section"),
        MultiFieldPanel([
            FieldPanel('intro_copy'),
            FieldPanel('student_intro'),
            FieldPanel('lessons_desc'),
        ], heading="Marketing Speak"),
        MultiFieldPanel([
            FieldPanel('teachers_guide'),
            SnippetChooserPanel('standards_alignment'),
            SnippetChooserPanel('time_estimate'),
            SnippetChooserPanel('program'),
            SnippetChooserPanel('audience'),
            SnippetChooserPanel('tag'),
            SnippetChooserPanel('topic')
        ], heading="Module Metadata")
    ]
    

    # def __str__(self):
    #     return self.title

    # def get_fields(self):
    #     return [(field.name, field.value_to_string(self)) for field in Module._meta.fields]
