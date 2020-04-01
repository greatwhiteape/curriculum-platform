from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel, PageChooserPanel)
from wagtail.images.edit_handlers import ImageChooserPanel


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

    feature1_copy = models.TextField(
      null=True,
      blank=True,
      help_text='Short copy blurb'
    )

    feature1_link = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Link to resource',
        on_delete=models.SET_NULL,
    )

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

    feature2_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature2_link = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Link to resource',
        on_delete=models.SET_NULL,
    )

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

    feature3_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature3_link = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Link to resource',
        on_delete=models.SET_NULL,
    )

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

    feature4_link = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Link to resource',
        on_delete=models.SET_NULL,
    )

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

    feature5_link = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Link to resource',
        on_delete=models.SET_NULL,
    )

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

    feature6_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Short copy blurb'
    )

    feature6_link = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Link to resource',
        on_delete=models.SET_NULL,
    )

    #LabVenture
    labventure_section_title = models.CharField(
      null=True,
      blank=True,
      max_length=255,
      help_text='Title to display above the promo copy'
    )

    labventure_section_copy = models.TextField(
      null=True,
      blank=True,
      max_length=255,
      help_text='Marketing copy for the Labventure.'
    )

    labventure_section_logo = models.ForeignKey(
      'wagtailimages.Image',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
      related_name='+'
    )

    labventure_section_hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    labventure_section_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        help_text='Text for call to action button (25 Characters Max).'
    )

    labventure_section_button_link = models.URLField(
      null=True,
      blank=True,
      help_text='Link that call to button action links to'
    )

    # labventure_section = models.ForeignKey(
    #     'wagtailcore.Page',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+',
    #     help_text='First featured section for the homepage. Will display up to '
    #     'three child items.',
    #     verbose_name='Labventure section'
    # )

    # Vital Signs Section
    vitalsigns_section_title = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text='Title to display above the promo copy'
    )

    vitalsigns_section_copy = models.TextField(
        null=True,
        blank=True,
        help_text='Marketing copy for the Vital Signs.'
    )

    vitalsigns_section_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    vitalsigns_section_hero = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    vitalsigns_section_button_text = models.CharField(
        null=True,
        blank=True,
        max_length=25,
        help_text='Text for call to action button (25 Characters Max).'
    )

    vitalsigns_section_button_link = models.URLField(
        null=True,
        blank=True,
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


    content_panels = Page.content_panels + [
        MultiFieldPanel([
          ImageChooserPanel('image'),
          FieldPanel('hero_text', classname="full"),
        ], heading="Hero section"),
        MultiFieldPanel([
          FieldPanel('featured_title'),
          FieldPanel('featured_copy'),
          MultiFieldPanel([
            FieldPanel('feature1_title'),
            FieldPanel('feature1_copy'),
            ImageChooserPanel('feature1_image'),
            PageChooserPanel('feature1_link'),
          ], heading="Feature 1"),
          MultiFieldPanel([
            FieldPanel('feature2_title'),
            FieldPanel('feature2_copy'),
            ImageChooserPanel('feature2_image'),
            PageChooserPanel('feature2_link'),
          ], heading="Feature 2"),
          MultiFieldPanel([
            FieldPanel('feature3_title'),
            FieldPanel('feature3_copy'),
            ImageChooserPanel('feature3_image'),
            PageChooserPanel('feature3_link'),
          ], heading="Feature 3"),
          MultiFieldPanel([
            FieldPanel('feature4_title'),
            FieldPanel('feature4_copy'),
            PageChooserPanel('feature4_link'),
          ], heading="Feature 4"),
          MultiFieldPanel([
            FieldPanel('feature5_title'),
            FieldPanel('feature5_copy'),
            PageChooserPanel('feature5_link'),
          ], heading="Feature 5"),
          MultiFieldPanel([
            FieldPanel('feature6_title'),
            FieldPanel('feature6_copy'),
            ImageChooserPanel('feature6_image'),
            PageChooserPanel('feature6_link'),
          ], heading="Feature 6"),
        ], heading="Featured Section"),
        MultiFieldPanel([
          FieldPanel('labventure_section_title'),
          FieldPanel('labventure_section_copy'),
          ImageChooserPanel('labventure_section_logo'),
          ImageChooserPanel('labventure_section_hero'),
          FieldPanel('labventure_section_button_text'),
          FieldPanel('labventure_section_button_link')
        ], heading="LabVenture"),
        MultiFieldPanel([
          FieldPanel('vitalsigns_section_title'),
          FieldPanel('vitalsigns_section_copy'),
          ImageChooserPanel('vitalsigns_section_logo'),
          ImageChooserPanel('vitalsigns_section_hero'),
          FieldPanel('vitalsigns_section_button_text'),
          FieldPanel('vitalsigns_section_button_link')
        ], heading="Vital Signs"),
        MultiFieldPanel([
          FieldPanel('gmri_section_title'),
          FieldPanel('gmri_section_copy'),
          ImageChooserPanel('gmri_section_logo'),
          ImageChooserPanel('gmri_section_hero'),
        ], heading="GMRI EDU"),
        MultiFieldPanel([
          MultiFieldPanel([
            FieldPanel('c2a_1_section_title'),
            FieldPanel('c2a_1_section_copy'),
            FieldPanel('c2a_1_section_button_text'),
            FieldPanel('c2a_1_section_button_link')
          ], heading="Call to Action 1"),
          MultiFieldPanel([
            FieldPanel('c2a_2_section_title'),
            FieldPanel('c2a_2_section_copy'),
            FieldPanel('c2a_2_section_button_text'),
            FieldPanel('c2a_2_section_button_link')
          ], heading="Call to Action 2"),
          MultiFieldPanel([
            FieldPanel('c2a_3_section_title'),
            FieldPanel('c2a_3_section_copy'),
            FieldPanel('c2a_3_section_button_text'),
            FieldPanel('c2a_3_section_button_link')
          ], heading="Call to Action 3")
        ], heading="Call to Action")
    ]

    # search_fields = [
    #     index.SearchField('first_name'),
    #     index.SearchField('last_name'),
    # ]

