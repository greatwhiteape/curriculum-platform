from django.db import models

from wagtail.core.fields import RichTextField
from wagtail.snippets.models import register_snippet

@register_snippet
class Activity(models.Model):
    class Meta:
        managed = True
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    createDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    teachers_guide = models.URLField()
    overview_copy = models.TextField(null=True, blank=True)
    student_copy = models.TextField(null=True, blank=True)
    link_to_activity = models.URLField()
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
    activity_type = models.ForeignKey(
        'taxonomy.ActivityType',
        null=True,
        blank=True,
        on_delete = models.SET_NULL
    )

    def __str__(self):
        return 'Guiding Reading: ' + self.title
