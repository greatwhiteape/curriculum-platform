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

class Lesson(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        
    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    hero_image = models.ImageField(
        upload_to='images/lessons/',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=100)
    subtitle = models.CharField(
        max_length=100,
        blank=True
    )    
    intro_copy = RichTextField(
        verbose_name="Marketing Copy",
        null=True,
        blank=True
    )
    student_intro = RichTextField(
        verbose_name="Copy for the Student Page",
        null=True, 
        blank=True
    )
    teachers_guide = models.URLField(
        null=True,
        blank=True
    )
    learning_outcomes = RichTextField(
        null=True,
        blank=True
    )
    standards_alignment = models.ManyToManyField(
        'taxonomy.Standard',
        blank=True
    )
    time_estimate = models.ForeignKey(
        'taxonomy.TimeEstimate',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    program = models.ManyToManyField(
        'taxonomy.Program',
        blank=True
    )
    audience = models.ManyToManyField(
        'taxonomy.Audience',
        blank=True
    )
    tag = models.ManyToManyField(
        'taxonomy.Tag', 
        blank=True
    )
    topic = models.ManyToManyField(
        'taxonomy.Topic',
        blank=True
    )

    def __str__(self):
        return self.title