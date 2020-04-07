from __future__ import unicode_literals
import requests

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
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.api import APIField

from modules.models import Module


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
    help_text='Section title'
  )

  featured_copy = models.TextField(
    null=True,
    blank=True,
    help_text='Featured content copy'
  )

  body = RichTextField(
    null=True, 
    blank=True, 
    help_text='Content Body'
  )

  content_panels = Page.content_panels + [
    MultiFieldPanel([
      ImageChooserPanel('image'),
      FieldPanel('hero_text', classname="full"),
    ], heading="Hero section"),
    MultiFieldPanel([
      FieldPanel('featured_title'),
      FieldPanel('featured_copy')
    ], heading="Featured Section"),
    MultiFieldPanel([
      FieldPanel('body', classname="full"),
    ], heading="Body")
  ]

  # Export fields over the API
  api_fields = [
    APIField('image'),
    APIField('hero_text'),
    APIField('featured_title'),
    APIField('featured_copy'),
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
    help_text='Section title'
  )

  featured_copy = models.TextField(
    null=True,
    blank=True,
    help_text='Featured content copy'
  )

  search_tag = models.TextField(
    null=True,
    blank=True,
    help_text='<app-root> tag plus modifiers like Program or modulesOnly'
  )

  content_panels = Page.content_panels + [
    MultiFieldPanel([
      ImageChooserPanel('image'),
      FieldPanel('hero_text', classname="full"),
    ], heading="Hero Section"),
    MultiFieldPanel([
      FieldPanel('featured_title'),
      FieldPanel('featured_copy'),
    ], heading="Featured Section"), 
    MultiFieldPanel([
      FieldPanel('search_tag'),
    ], heading="Angular Application Tag")
  ]

  # Export fields over the API
  api_fields = [
    APIField('image'),
    APIField('hero_text'),
    APIField('featured_title'),
    APIField('featured_copy'),
    APIField('search_tag'),
  ]

  def serve(self, request):
    modules = Module.objects.all()
    self.modules = modules
    return super().serve(request)
