from wagtail.api.v2.views import BaseAPIViewSet

from .models import Module


class ModulesAPIEndpoint(BaseAPIViewSet):
    model = Module

    body_fields = BaseAPIViewSet.body_fields + [
        'live',
        # SETH
        'slug',
        'title',
        'subtitle',
        'intro_copy',
        'hero_image',
        'overview_copy',
        'student_intro',
        'learning_outcomes',
        'teachers_guide',
        'teachers_desc',
        'students_desc',
        'program',
        'time_estimate',
        'audience_relationship',
        'learningspace_relationship',
        'standards_relationship',
        'topic_relationship',
        'tag_relationship',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        'live',
        # SETH
        'slug',
        'title',
        'subtitle',
        'hero_image',
        'intro_copy',
        'hero_image',
        'overview_copy',
        'overview_copy',
        'learning_outcomes',
        'teachers_guide',
        'teachers_desc',
        'students_desc',
        'program',
        'time_estimate',
        'audience_relationship',
        'learningspace_relationship',
        'standards_relationship',
        'topic_relationship',
        'tag_relationship',
    ]
