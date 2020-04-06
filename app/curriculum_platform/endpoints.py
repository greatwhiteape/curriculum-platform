from wagtail.api.v2.endpoints import BaseAPIEndpoint

from modules.models import Module


class ModulesAPIEndpoint(BaseAPIEndpoint):
    model = Module

    body_fields = BaseAPIEndpoint.body_fields + [
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
        # 'audience',
        # 'standards_alignment',
        # 'topics',
        # 'tags',
    ]

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
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
        'audience',
        'standards_alignment',
        'topics',
        # 'tags',
    ]