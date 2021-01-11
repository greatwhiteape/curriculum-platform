from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.core.fields import RichTextField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

@register_snippet
class Program(models.Model):
    program_name = models.CharField(max_length=100)
    program_description = RichTextField(null=True, blank=True)
    program_url = models.URLField(null=True)
    program_color = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.program_name

    class Meta:
        verbose_name = "Program"
        verbose_name_plural = "Programs"

    api_fields = [
        APIField('program_name'),
        APIField('program_description'),
        APIField('program_url'),
        APIField('program_color'),
    ]

@register_snippet
class StandardsBody(models.Model):
    class Meta:
        verbose_name_plural = "Standards Bodies"

    standards_body = models.CharField(max_length=100)
    standards_body_url = models.URLField(null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.standards_body

@register_snippet
class Standard(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Standard'
        verbose_name_plural = 'Standards'

    standard = models.CharField(max_length=200)
    standard_group = models.ForeignKey(StandardsBody, on_delete=models.PROTECT)
    standard_link = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s %s' % (self.standard_group, self.standard)

@register_snippet
class Audience(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Intended Age Range'
        verbose_name_plural = 'Intended Age Ranges'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    age_range = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.age_range

@register_snippet
class Topic(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    topic = models.CharField(max_length=50)

    def __str__(self):
        return self.topic

@register_snippet
class AssetType(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Type of Asset'
        verbose_name_plural = 'Type of Assets'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    asset_type = models.CharField(max_length=50)

    def __str__(self):
        return self.asset_type

@register_snippet
class Tag(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

@register_snippet
class TimeEstimate(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Time Estimate'
        verbose_name_plural = 'Time Estimates'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    time_estimate = models.CharField(max_length=200)

    def __str__(self):
        return self.time_estimate

@register_snippet
class ActivityType(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Type of Activity'
        verbose_name_plural = 'Type of Activities'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    activity_type = models.CharField(max_length=50)

    def __str__(self):
        return self.activity_type

@register_snippet
class LearningSpace(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Learning Space'
        verbose_name_plural = 'Learning Space'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    learning_space = models.CharField(max_length=50)

    def __str__(self):
        return self.learning_space
