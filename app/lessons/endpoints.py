from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Lesson


class LessonsAPIEndpoint(BaseAPIEndpoint):
    model = Lesson

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
        'lesson_audience_relationship',
        'lesson_standards_relationship',
        'lesson_topic_relationship',
        'lesson_tag_relationship',
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
        'lesson_audience_relationship',
        'lesson_standards_relationship',
        'lesson_topic_relationship',
        'lesson_tag_relationship',
    ]