from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Activity


class ActivitiesAPIEndpoint(BaseAPIEndpoint):
    model = Activity
    
    body_fields = BaseAPIEndpoint.body_fields + [
        "title",
        # "teachers_guide",
        "overview_copy",
        "student_copy",
        "internal_link",
        "external_link",
        "program",
        "audience",
        "activity_type",
        "topic",
        'activity_tag_relationship',
    ]