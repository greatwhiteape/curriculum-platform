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
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from .blocks import hpQuoteBlock, hpActivityBlock, hpAssetBlock, hpModuleBlock

class HomePage(Page):

    template="home/home_page.html"

    # Hero section of HomePage
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

    featured_items = StreamField(
        [
            ('quote', hpQuoteBlock()),
            ('module', hpModuleBlock()),
            ('activity', hpActivityBlock()),
            ('asset', hpAssetBlock())
        ],
        null=True,
        blank=True,
        verbose_name="Lessons Tab Content",
    )

    #LabVenture
    labventure_section_title = models.CharField(
      null=True,
      blank=True,
      max_length=255,
      verbose_name = 'LabVenture Section Title',
      help_text='Title to display above the promo copy'
    )

    labventure_section_copy = models.TextField(
      null=True,
      blank=True,
      max_length=255,
      verbose_name = 'LabVenture Section Copy',
      help_text='Marketing copy for the Labventure.'
    )

    labventure_section_logo = models.ForeignKey(
      'wagtailimages.Image',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      verbose_name = 'LabVenture Section Logo',
      related_name='+'
    )

    labventure_section_hero = models.ForeignKey(
      'wagtailimages.Image',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      verbose_name = 'LabVenture Section Hero Image',
      related_name='+'
    )

    labventure_section_hero_alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Alt-tag for image'
    )

    labventure_section_button_text = models.CharField(
      null=True,
      blank=True,
      max_length=25,
      verbose_name = 'LabVenture Call to Action Button Text',
      help_text='Text for call to action button (25 Characters Max).'
    )

    labventure_section_button_link = models.URLField(
      null=True,
      blank=True,
      verbose_name = 'LabVenture Button Link',
      help_text='Link that call to button action links to'
    )
    # Vital Signs Section
    vitalsigns_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name = 'Citizen Science Section Title',
        help_text='Title to display above the promo copy'
    )

    vitalsigns_section_copy = models.TextField(
        null=True,
        blank=True,
        verbose_name = 'Citizen Science Copy',
        help_text='Marketing copy for the Vital Signs.'
    )

    vitalsigns_section_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name = 'Citizen Science Logo',
        related_name='+'
    )

    vitalsigns_section_hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name = 'Citizen Science Hero Image',
        related_name='+'
    )

    vitalsigns_section_hero_alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Alt-tag for image'
    )

    vitalsigns_section_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        verbose_name = 'Citizen Science Call to Action Button Text',
        help_text='Text for call to action button (25 Characters Max).'
    )

    vitalsigns_section_button_link = models.URLField(
        null=True,
        blank=True,
        verbose_name = 'Citizen Science Button Link',
        help_text='Link that call to button action links to'
    )

    # GMRI EDU general marketing
    gmri_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    gmri_section_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Marketing copy for the GMRI.'
    )

    gmri_section_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    gmri_section_hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    gmri_section_hero_alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Alt-tag for image'
    )


    content_panels = Page.content_panels + [
        MultiFieldPanel([
          ImageChooserPanel('image'),
          FieldPanel('hero_text', classname="full"),
        ], heading="Header Section"),
        MultiFieldPanel([
          FieldPanel('featured_title'),
          FieldPanel('featured_copy'),
          StreamFieldPanel('featured_items'),
        ], heading="Featured Section", classname='wagtailuiplus__panel--collapsed'),
        MultiFieldPanel([
          FieldPanel('labventure_section_title'),
          FieldPanel('labventure_section_copy'),
          ImageChooserPanel('labventure_section_logo'),
          ImageChooserPanel('labventure_section_hero'),
          FieldPanel('labventure_section_hero_alt'),
          FieldPanel('labventure_section_button_text'),
          FieldPanel('labventure_section_button_link')
        ], heading="LabVenture", classname='wagtailuiplus__panel--collapsed'),
        MultiFieldPanel([
          FieldPanel('vitalsigns_section_title'),
          FieldPanel('vitalsigns_section_copy'),
          ImageChooserPanel('vitalsigns_section_logo'),
          ImageChooserPanel('vitalsigns_section_hero'),
          FieldPanel('vitalsigns_section_hero_alt'),
          FieldPanel('vitalsigns_section_button_text'),
          FieldPanel('vitalsigns_section_button_link')
        ], heading="Citizen Science", classname='wagtailuiplus__panel--collapsed'),
        MultiFieldPanel([
          FieldPanel('gmri_section_title'),
          FieldPanel('gmri_section_copy'),
          ImageChooserPanel('gmri_section_logo'),
          ImageChooserPanel('gmri_section_hero'),
          FieldPanel('gmri_section_hero_alt'),
        ], heading="GMRI EDU", classname='wagtailuiplus__panel--collapsed'),
    ]
