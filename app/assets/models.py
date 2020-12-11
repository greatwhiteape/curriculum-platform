from django.db import models
from django.core.exceptions import ValidationError

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
    AssetTypeSerializer,
    LearningSpaceSerializer,
)


@register_snippet
class Asset(ClusterableModel):
    class Meta:
        verbose_name = "Curriculum Asset"
        verbose_name_plural = "Curriculum Assets"

    template = "assets/asset_page.html"

    live = models.BooleanField(
        verbose_name='Publish',
        default=False,
        editable=True
    )
    slug = models.SlugField(
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)

    asset_link = StreamField(
        [
            ('image', ImageChooserBlock()),
            ('document', DocumentChooserBlock()),
            ('external', blocks.Link()),
            ('google_doc', blocks.GoogleDocEmbed()),
            ('codap', blocks.CODAPEmbed()),
            ('video', blocks.YouTubeBlock()),
            ('embed', EmbedBlock()),
            ('raw_html', wagtail_blocks.RawHTMLBlock()),
        ],
        null=True,
        blank=True
    )
    program = models.ForeignKey(
        'taxonomy.Program',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='+',
    )
    asset_type = models.ForeignKey(
        'taxonomy.AssetType',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    student_asset = models.BooleanField(null=True)
    student_intro = RichTextField(
        verbose_name="Copy for the Student Page",
        null=True,
        blank=True
    )
    audience = models.ForeignKey(
        'taxonomy.Audience',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+',
    )
    time_estimate = models.ForeignKey(
        'taxonomy.TimeEstimate',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )

    @property
    def audience(self):
        audience = [
            n.audience for n in self.audience_relationship.all()
        ]
        return audience

    @property
    def learning_spaces(self):
        learning_spaces = [
            n.learning_space for n in self.learningspace_relationship.all()
        ]
        return tags

    @property
    def tags(self):
        tags = [
            n.tag for n in self.tag_relationship.all()
        ]
        return tags

    @property
    def topics(self):
        topics = [
            n.topic for n in self.topic_relationship.all()
        ]
        return topics


    def __str__(self):
        return self.title


    panels = [
      FieldPanel("live"),
      FieldPanel('slug'), # SETH
      FieldPanel("title"),
      FieldPanel("description"),
      FieldPanel("asset_type"),
      FieldPanel("student_asset"),
      FieldPanel("student_intro"),
      StreamFieldPanel('asset_link'),
      SnippetChooserPanel("program"),
      SnippetChooserPanel('time_estimate'),
      InlinePanel('audience_relationship', label="Audience"),
      InlinePanel('learning_space', label="Learning Space"),
      InlinePanel('standards_relationship', label="Standards Alignment"),
      InlinePanel('topic_relationship', label="Topics"),
      InlinePanel('tag_relationship', label="Tags"),
    ]

    api_fields = [
        APIField("live"),
        APIField("description"),
        APIField("student_asset"),
        APIField("asset_link"),
        APIField("program", serializer=ProgramSerializer()),
        APIField("audience", serializer=AudienceSerializer()),
        APIField("asset_type", serializer=AssetTypeSerializer()),
        APIField("topic", serializer=TopicSerializer()),
        APIField('asset_tag_relationship', serializer=TagSerializer()),
        APIField("learning_space", serializer=LearningSpaceSerializer())
    ]

class AssetTagRelationship(models.Model):
  asset = ParentalKey(
      'Asset',
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

class AssetAudienceRelationship(models.Model):
  module = ParentalKey(
      'Asset',
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

class AssetLearningSpaceRelationship(models.Model):
  asset = ParentalKey(
      'Asset',
      related_name='learningspace_relationship'
  )
  learning_space = models.ForeignKey(
      'taxonomy.LearningSpace',
      null=True,
      blank=True,
      on_delete=models.SET_NULL,
  )

  panels = [
      FieldPanel('learning_space')
  ]

  api_fields = [
      APIField('learning_space', serializer=LearningSpaceSerializer())
  ]

class AssetStandardsRelationship(models.Model):
  module = ParentalKey(
      'Asset',
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

class AssetTopicRelationship(models.Model):
  module = ParentalKey(
      'Asset',
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
