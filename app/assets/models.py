from django.db import models
from django.core.exceptions import ValidationError

from wagtail.api import APIField

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel


from taxonomy.serializers import (
    ProgramSerializer, 
    TimeEstimateSerializer, 
    AudienceSerializer, 
    StandardsSerializer, 
    TopicSerializer, 
    TagSerializer,
    AssetTypeSerializer,
)
@register_snippet
class Asset(models.Model):
    class Meta: 
        verbose_name = "Curriculum Asset"
        verbose_name_plural = "Curriculum Assets"


    template = "assets/asset_page.html"

    title = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)

    internal_link = models.ForeignKey(
        'wagtaildocs.Document',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an internal Wagtail page',
        on_delete=models.SET_NULL,
    )
    external_link = models.URLField(blank=True)

    program = models.ForeignKey(
        'taxonomy.Program',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
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
    audience = models.ForeignKey(
        'taxonomy.Audience',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='+',
    )
    # tag = models.ForeignKey(
    #     'taxonomy.Tag', 
    #     on_delete=models.SET_NULL, 
    #     null=True, 
    #     blank=True,
    #     related_name='+',
    # )
    # topic = models.ForeignKey(
    #     'taxonomy.Topic',
    #     on_delete=models.SET_NULL, 
    #     null=True, 
    #     blank=True,
    #     related_name='+',
    # )

    def __str__(self):
        return self.title


    panels = [
        FieldPanel("description"),
        FieldPanel("student_asset"),
        DocumentChooserPanel("internal_link"),
        FieldPanel("external_link"),
        SnippetChooserPanel("program"),
        SnippetChooserPanel("audience"),
        SnippetChooserPanel("asset_type"),
        # SnippetChooserPanel("tag"),
        # SnippetChooserPanel("topic"),
    ]

    api_fields = [
        APIField("description"),
        APIField("student_asset"),
        APIField("internal_link"),
        APIField("external_link"),
        APIField("program", serializer=ProgramSerializer()),
        APIField("audience", serializer=AudienceSerializer()),
        APIField("asset_type", serializer=AssetTypeSerializer()),
        # APIField("tag"),
        # APIField("topic"),
    ]

    

    def clean(self):
        super().clean()

        if self.internal_link and self.external_link:
            # Both fields are filled out...
            raise ValidationError({
                'internal_link': ValidationError("Please only select a document OR enter an external URL"),
                'external_link': ValidationError("Please only select a document OR enter an external URL"),
            })

        if not self.internal_link and not self.external_link:
            raise ValidationError({
                'internal_link':ValidationError("You must always select a document OR enter an external URL."),
                'external_link':ValidationError("You must always select a document OR enter an external URL."),
            })