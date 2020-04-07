from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Module


class ModulesAPIEndpoint(BaseAPIEndpoint):
    model = Module

    body_fields = BaseAPIEndpoint.body_fields + [
        'title',
        'subtitle',
        'hero_image',
        'intro_copy',
        'student_intro',
        'learning_outcomes',
        'teachers_guide',
        'teachers_desc',
        'students_desc',
        'program',
        'time_estimate',
        'module_audience_relationship',
        'module_standards_relationship',
        'module_topic_relationship',
        'module_tag_relationship',
    ]

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
        'title',
        'subtitle',
        'hero_image',
        'intro_copy',
        'student_intro',
        'learning_outcomes',
        'teachers_guide',
        'teachers_desc',
        'students_desc',
        'program',
        'time_estimate',
        'module_audience_relationship',
        'module_standards_relationship',
        'module_topic_relationship',
        'module_tag_relationship',
    ]