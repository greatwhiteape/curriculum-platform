from __future__ import unicode_literals
import requests

from django import forms

from django.db import models
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


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
from wagtail.core import blocks as wagtail_blocks
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.api import APIField

from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock

from modules.models import Module

from streams import blocks

from taxonomy.serializers import (
    ProgramSerializer,
    TimeEstimateSerializer,
    AudienceSerializer,
    StandardsSerializer,
    TopicSerializer,
    TagSerializer,
)

class ContentPage(Page):
  class Meta:
    managed = True
    verbose_name = 'Content'
    verbose_name_plural = 'Content Pages'

  image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+',
    help_text='Homepage image'
  )

  image_alt = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    help_text='Alt tag for image'
  )

  hero_text = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    help_text='Marketing-speak about GRMI EDU (100 Characters Max)'
  )

  program = models.ForeignKey(
    'taxonomy.Program',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
  )

  featured_title = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    verbose_name='Introduction Title',
    help_text='Title for intro copy (optional)'
  )

  featured_copy = RichTextField(
    features=['bold', 'italic', 'link', 'ol', 'ul', 'document-link', 'image'],
    null=True,
    blank=True,
    verbose_name='Introductory Content Copy',
    help_text='Copy describing the program & the featured curricula'
  )

  body = StreamField(
      [
        ('title', blocks.TitleBlock()),
        ('copy', wagtail_blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('asset', SnippetChooserBlock('assets.Asset')),
        ('activity', SnippetChooserBlock('activity.Activity')),
        ('document', DocumentChooserBlock()),
        ('embed', EmbedBlock()),
        ('header', HeaderBlock()),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
        ('map', MapBlock()),
      ],
      null=True,
      blank=True
  )

  content_panels = Page.content_panels + [
    MultiFieldPanel([
      ImageChooserPanel('image'),
      FieldPanel('image_alt'),
      FieldPanel('hero_text', classname="full"),
    ], heading="Hero section"),
    MultiFieldPanel([
      FieldPanel('featured_title'),
      FieldPanel('featured_copy'),
    ], heading="Introduction Section", classname='wagtailuiplus__panel--collapsed'),
    MultiFieldPanel([
      StreamFieldPanel('body'),
      SnippetChooserPanel('program'),
    ], heading="Body")
  ]

  # Export fields over the API
  api_fields = [
    APIField('image'),
    APIField('image_alt'),
    APIField('hero_text'),
    APIField('featured_title'),
    APIField('featured_copy'),
    APIField('program'),
    APIField('body'),
  ]

  def serve(self, request):
    modules = Module.objects.all()
    self.modules = modules
    return super().serve(request)


class SearchPage(Page):
  class Meta:
    managed = True
    verbose_name = 'Search'
    verbose_name_plural = 'Search Pages'

  image = models.ForeignKey(
    'wagtailimages.Image',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='+',
    help_text='Homepage image'
  )

  image_alt = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    help_text='Alt tag for image'
  )

  hero_text = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    help_text='Marketing-speak about GRMI EDU (100 Characters Max)'
  )

  featured_title = models.CharField(
    max_length=100,
    null=True,
    blank=True,
    verbose_name='Introduction Title',
    help_text='Title for intro copy (optional)'
  )

  featured_copy = RichTextField(
    features=['bold', 'italic', 'link', 'ol', 'ul', 'document-link', 'image'],
    null=True,
    blank=True,
    verbose_name='Introductory Content Copy',
    help_text='Copy describing the program & the featured curricula'
  )

  search_tag = models.TextField(
    null=True,
    blank=True,
    help_text='<app-root> tag plus modifiers like Program or modulesOnly'
  )

  program = models.ForeignKey(
    'taxonomy.Program',
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
  )

  content_panels = Page.content_panels + [
    MultiFieldPanel([
      ImageChooserPanel('image'),
      FieldPanel('image_alt'),
      FieldPanel('hero_text', classname="full"),
    ], heading="Hero Section"),
    MultiFieldPanel([
      FieldPanel('featured_title'),
      FieldPanel('featured_copy'),
    ], heading="Introduction Section"),
    MultiFieldPanel([
      FieldPanel('search_tag'),
      SnippetChooserPanel('program'),
    ], heading="Angular Application Tag")
  ]

  # Export fields over the API
  api_fields = [
    APIField('image'),
    APIField('image_alt'),
    APIField('hero_text'),
    APIField('featured_title'),
    APIField('featured_copy'),
    APIField('search_tag'),
    APIField('program'),
  ]

  def serve(self, request):
    modules = Module.objects.all()
    self.modules = modules
    return super().serve(request)
