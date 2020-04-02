from django.db import models

from wagtail.core.fields import RichTextField

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


# class DataTask(models.Model):
#     createDate = models.DateTimeField(auto_now_add=True)
#     modifiedDate = models.DateTimeField(auto_now=True)
#     title = models.CharField(max_length=50)
#     teachers_guide = models.URLField(
#         null=True,
#         blank=True,)
#     overview_copy = models.TextField(null=True, blank=True)
#     student_copy = models.TextField(null=True, blank=True)
#     time_estimate = models.ForeignKey(
#         'taxonomy.TimeEstimate',
#         null=True,
#         blank=True,
#         on_delete = models.SET_NULL
#     )
#     program = models.ManyToManyField(
#         'taxonomy.Program',
#         blank=True
#     )
#     audience = models.ManyToManyField(
#         'taxonomy.Audience',
#         blank=True
#     )
#     tag = models.ManyToManyField(
#         'taxonomy.Tag', 
#         blank=True
#     )
#     topic = models.ManyToManyField(
#         'taxonomy.Topic',
#         blank=True
#     )

#     def __str__(self):
#         return 'Data Task: ' + self.title


# class MiniLesson(models.Model):
#     class Meta:
#         managed = True
#         verbose_name = 'Mini-Lesson'
#         verbose_name_plural = 'Mini-Lessons'

#     createDate = models.DateTimeField(auto_now_add=True)
#     modifiedDate = models.DateTimeField(auto_now=True)
#     title = models.CharField(max_length=100)
#     display_title = models.CharField(
#         max_length=100,
#         blank=True
#     )    
#     teachers_guide = models.URLField(
#         null=True,
#         blank=True,)
#     overview_copy = models.TextField(null=True, blank=True)
#     student_copy = models.TextField(null=True, blank=True)
#     time_estimate = models.ForeignKey(
#         'taxonomy.TimeEstimate',
#         null=True,
#         blank=True,
#         on_delete = models.SET_NULL
#     )
#     program = models.ManyToManyField(
#         'taxonomy.Program',
#         blank=True
#     )
#     audience = models.ManyToManyField(
#         'taxonomy.Audience',
#         blank=True
#     )
#     tag = models.ManyToManyField(
#         'taxonomy.Tag', 
#         blank=True
#     )
#     topic = models.ManyToManyField(
#         'taxonomy.Topic',
#         blank=True
#     )

#     def __str__(self):
#         return 'Mini-Lesson: ' + self.title


# class TakeAction(models.Model):
#     class Meta:
#         managed = True
#         verbose_name = 'Take Action Activity'
#         verbose_name_plural = 'Take Action Activities'

#     createDate = models.DateTimeField(auto_now_add=True)
#     modifiedDate = models.DateTimeField(auto_now=True)
#     title = models.CharField(max_length=50)
#     teachers_guide = models.URLField(
#         null=True,
#         blank=True,)
#     overview_copy = models.TextField(null=True, blank=True)
#     student_copy = models.TextField(null=True, blank=True)
#     time_estimate = models.ForeignKey(
#         'taxonomy.TimeEstimate',
#         null=True,
#         blank=True,
#         on_delete = models.SET_NULL
#     )
#     program = models.ManyToManyField(
#         'taxonomy.Program',
#         blank=True
#     )
#     audience = models.ManyToManyField(
#         'taxonomy.Audience',
#         blank=True
#     )
#     tag = models.ManyToManyField(
#         'taxonomy.Tag', 
#         blank=True
#     )
#     topic = models.ManyToManyField(
#         'taxonomy.Topic',
#         blank=True
#     )

#     def __str__(self):
#         return 'Take Action: ' + self.title