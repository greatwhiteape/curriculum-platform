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


@register_snippet
class People(index.Indexed, ClusterableModel):
    first_name = models.CharField("First name", max_length=254)
    last_name = models.CharField("Last name", max_length=254)
    job_title = models.CharField("Job title", max_length=254)

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('job_title'),
        ImageChooserPanel('image')
    ]

    search_fields = [
        index.SearchField('first_name'),
        index.SearchField('last_name'),
    ]

    @property
    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:
            return ''

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'


@register_snippet
class FooterText(models.Model):
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = 'Footer Text'



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

    #Featured Elements
    #Feature 1
    feature1_title = models.CharField(
      null=True,
      blank=True,
      max_length= 50,
      help_text='LabVenture Block 1'
    )

    feature1_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    feature1_image_alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Alt-tag for image'
    )

    feature1_copy = models.TextField(
      null=True,
      blank=True,
      help_text='Short copy blurb'
    )

    feature1_link = models.URLField(
      null=True,
      blank=True,
      help_text='Link that call to button action links to'
    )

    # feature1_link = models.ForeignKey(
    #     'modules.Module',
    #     blank=True,
    #     null=True,
    #     related_name='+',
    #     help_text='Link to resource',
    #     on_delete=models.SET_NULL,
    # )

    #Feature 2
    feature2_title = models.CharField(
        null=True,
        blank=True,
        max_length= 50,
        help_text='LabVenture Block 2'
    )

    feature2_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    feature2_image_alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Alt-tag for image'
    )

    feature2_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature2_link = models.URLField(
      null=True,
      blank=True,
      help_text='Link that call to button action links to'
    )

    # feature2_link = models.ForeignKey(
    #     'modules.Module',
    #     blank=True,
    #     null=True,
    #     related_name='+',
    #     help_text='Link to resource',
    #     on_delete=models.SET_NULL,
    # )

    #Feature 3
    feature3_title = models.CharField(
        null=True,
        blank=True,
        max_length= 50,
        help_text='LabVenture Block 3'
    )

    feature3_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    feature3_image_alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Alt-tag for image'
    )

    feature3_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature3_link = models.URLField(
      null=True,
      blank=True,
      help_text='Link that call to button action links to'
    )

    # feature3_link = models.ForeignKey(
    #     'lessons.Lesson',
    #     blank=True,
    #     null=True,
    #     related_name='+',
    #     help_text='Link to resource',
    #     on_delete=models.SET_NULL,
    # )

    #Feature 4
    feature4_title = models.CharField(
        null=True,
        blank=True,
        max_length= 50,
        help_text='LabVenture Block 4'
    )

    feature4_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature4_link = models.URLField(
      null=True,
      blank=True,
      help_text='Link that call to button action links to'
    )

    # feature4_link = models.ForeignKey(
    #     'activity.Activity',
    #     blank=True,
    #     null=True,
    #     related_name='+',
    #     help_text='Link to resource',
    #     on_delete=models.SET_NULL,
    # )

    #Feature 5
    feature5_title = models.CharField(
        null=True,
        blank=True,
        max_length= 50,
        help_text='LabVenture Block 5'
    )

    feature5_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature5_link = models.URLField(
      null=True,
      blank=True,
      help_text='Link that call to button action links to'
    )

    # feature5_link = models.ForeignKey(
    #     'activity.Activity',
    #     blank=True,
    #     null=True,
    #     related_name='+',
    #     help_text='Link to resource',
    #     on_delete=models.SET_NULL,
    # )

    #Feature 6
    feature6_title = models.CharField(
        null=True,
        blank=True,
        max_length= 50,
        help_text='LabVenture Block 6'
    )

    feature6_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    feature6_image_alt = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text='Alt-tag for image'
    )

    feature6_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature6_link = models.URLField(
      null=True,
      blank=True,
      help_text='Link that call to button action links to'
    )

    # feature6_link = models.ForeignKey(
    #     'lessons.Lesson',
    #     blank=True,
    #     null=True,
    #     related_name='+',
    #     help_text='Link to resource',
    #     on_delete=models.SET_NULL,
    # )

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

    # Call to action section

    # C2A_1
    c2a_1_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    c2a_1_section_copy = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Marketing copy (255 Characters Max - Optional).'
    )

    c2a_1_section_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        help_text='Text for call to action button (25 Characters Max).'
    )

    c2a_1_section_button_link = models.URLField(
        null=True,
        blank=True,
        help_text='Link that call to button action links to'
    )

    c2a_1_section_active = models.BooleanField(
      default=True,
      help_text='Enable or disable this box.'
    )

  # C2A_2
    c2a_2_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    c2a_2_section_copy = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Marketing copy (255 Characters Max - Optional).'
    )

    c2a_2_section_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        help_text='Text for call to action button (25 Characters Max).'
    )

    c2a_2_section_button_link = models.URLField(
        null=True,
        blank=True,
        help_text='Link that call to button action links to'
    )

    c2a_2_section_active = models.BooleanField(
      default=True,
      help_text='Enable or disable this box.'
    )

    # C2A_3
    c2a_3_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    c2a_3_section_copy = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Marketing copy (255 Characters Max - Optional).'
    )

    c2a_3_section_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        help_text='Text for call to action button (25 Characters Max).'
    )

    c2a_3_section_button_link = models.URLField(
        null=True,
        blank=True,
        help_text='Link that call to button action links to'
    )

    c2a_3_section_active = models.BooleanField(
      default=True,
      help_text='Enable or disable this box.'
    )



    feature1_image_alt


    content_panels = Page.content_panels + [
        MultiFieldPanel([
          ImageChooserPanel('image'),
          FieldPanel('hero_text', classname="full"),
        ], heading="Header Section"),
        MultiFieldPanel([
          FieldPanel('featured_title'),
          FieldPanel('featured_copy'),
          MultiFieldPanel([
            FieldPanel('feature1_title'),
            FieldPanel('feature1_copy'),
            ImageChooserPanel('feature1_image'),
            FieldPanel('feature1_image_alt'),
            FieldPanel('feature1_link'),
            # SnippetChooserPanel('feature1_link'),
          ], heading="Feature 1"),
          MultiFieldPanel([
            FieldPanel('feature2_title'),
            FieldPanel('feature2_copy'),
            ImageChooserPanel('feature2_image'),
            FieldPanel('feature2_image_alt'),
            FieldPanel('feature2_link'),
            # SnippetChooserPanel('feature2_link'),
          ], heading="Feature 2"),
          MultiFieldPanel([
            FieldPanel('feature3_title'),
            FieldPanel('feature3_copy'),
            ImageChooserPanel('feature3_image'),
            FieldPanel('feature3_image_alt'),
            FieldPanel('feature3_link'),
            # SnippetChooserPanel('feature3_link'),
          ], heading="Feature 3"),
          MultiFieldPanel([
            FieldPanel('feature4_title'),
            FieldPanel('feature4_copy'),
            FieldPanel('feature4_link'),
            # SnippetChooserPanel('feature4_link'),
          ], heading="Feature 4"),
          MultiFieldPanel([
            FieldPanel('feature5_title'),
            FieldPanel('feature5_copy'),
            FieldPanel('feature5_link'),
            # SnippetChooserPanel('feature5_link'),
          ], heading="Feature 5"),
          MultiFieldPanel([
            FieldPanel('feature6_title'),
            FieldPanel('feature6_copy'),
            ImageChooserPanel('feature6_image'),
            FieldPanel('feature6_image_alt'),
            FieldPanel('feature6_link'),
            # SnippetChooserPanel('feature6_link'),
          ], heading="Feature 6"),
        ], heading="Featured Section"),
        MultiFieldPanel([
          FieldPanel('labventure_section_title'),
          FieldPanel('labventure_section_copy'),
          ImageChooserPanel('labventure_section_logo'),
          ImageChooserPanel('labventure_section_hero'),
          FieldPanel('labventure_section_hero_alt'),
          FieldPanel('labventure_section_button_text'),
          FieldPanel('labventure_section_button_link')
        ], heading="LabVenture"),
        MultiFieldPanel([
          FieldPanel('vitalsigns_section_title'),
          FieldPanel('vitalsigns_section_copy'),
          ImageChooserPanel('vitalsigns_section_logo'),
          ImageChooserPanel('vitalsigns_section_hero'),
          FieldPanel('vitalsigns_section_hero_alt'),
          FieldPanel('vitalsigns_section_button_text'),
          FieldPanel('vitalsigns_section_button_link')
        ], heading="Citizen Science"),
        MultiFieldPanel([
          FieldPanel('gmri_section_title'),
          FieldPanel('gmri_section_copy'),
          ImageChooserPanel('gmri_section_logo'),
          ImageChooserPanel('gmri_section_hero'),
          FieldPanel('gmri_section_hero_alt'),
        ], heading="GMRI EDU"),
        MultiFieldPanel([
          MultiFieldPanel([
            FieldPanel('c2a_1_section_title'),
            FieldPanel('c2a_1_section_copy'),
            FieldPanel('c2a_1_section_button_text'),
            FieldPanel('c2a_1_section_button_link'),
            FieldPanel('c2a_1_section_active')
          ], heading="Call to Action 1"),
          MultiFieldPanel([
            FieldPanel('c2a_2_section_title'),
            FieldPanel('c2a_2_section_copy'),
            FieldPanel('c2a_2_section_button_text'),
            FieldPanel('c2a_2_section_button_link'),
            FieldPanel('c2a_2_section_active')
          ], heading="Call to Action 2"),
          MultiFieldPanel([
            FieldPanel('c2a_3_section_title'),
            FieldPanel('c2a_3_section_copy'),
            FieldPanel('c2a_3_section_button_text'),
            FieldPanel('c2a_3_section_button_link'),
            FieldPanel('c2a_3_section_active')
          ], heading="Call to Action 3")
        ], heading="Call to Action")
    ]

    # search_fields = [
    #     index.SearchField('first_name'),
    #     index.SearchField('last_name'),
    # ]

