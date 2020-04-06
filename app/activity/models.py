from django.db import models
from django.core.exceptions import ValidationError

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.documents.models import Document
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

@register_snippet
class Activity(ClusterableModel):
    class Meta:
        managed = True
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    # teachers_guide = models.URLField()
    overview_copy = RichTextField(null=True, blank=True)
    student_copy = RichTextField(null=True, blank=True)
    # link_to_activity = models.URLField()

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
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    time_estimate = models.ForeignKey(
        'taxonomy.TimeEstimate',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    audience = models.ForeignKey(
        'taxonomy.Audience',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    topic = models.ForeignKey(
        'taxonomy.Topic',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    activity_type = models.ForeignKey(
        'taxonomy.ActivityType',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )
    
    @property
    def tags(self):
        tags = [
            n.tag for n in self.lesson_tag_relationship.all()
        ]
        return tags

    # tag = models.ManyToManyField(
    #     'taxonomy.Tag', 
    #     blank=True
    # )

    def __str__(self):
        return self.title


    panels = [
        FieldPanel("title"),
        # FieldPanel("teachers_guide"),
        FieldPanel("overview_copy"),
        FieldPanel("student_copy"),
        DocumentChooserPanel("internal_link"),
        FieldPanel("external_link"),
        SnippetChooserPanel("program"),
        SnippetChooserPanel("audience"),
        SnippetChooserPanel("activity_type"),
        SnippetChooserPanel("topic"),
        # SnippetChooserPanel("tag"),
        InlinePanel('activity_tag_relationship', label="Tags"),
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
class ActivityTagRelationship(models.Model):
    activity = ParentalKey(
        'Activity',
        related_name='activity_tag_relationship'
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
