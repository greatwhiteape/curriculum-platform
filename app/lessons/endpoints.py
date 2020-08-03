from wagtail.api.v2.views import BaseAPIViewSet

from .models import Lesson


class LessonsAPIEndpoint(BaseAPIViewSet):
    model = Lesson

    body_fields = BaseAPIViewSet.body_fields + [
        'live',
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
        'standards_relationship',
        'topic_relationship',
        'tag_relationship',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        'live',
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
        'standards_relationship',
        'topic_relationship',
        'tag_relationship',
    ]
