from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Activity


class ActivitiesAPIEndpoint(BaseAPIEndpoint):
    model = Activity

    body_fields = BaseAPIEndpoint.body_fields + [
        "title",
        "overview_copy",
        "teachers_desc",
        "students_desc",
        "program",
        "audience",
        "activity_type",
        "topic",
        'tag_relationship',
    ]

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
        "title",
        "overview_copy",
        "teachers_desc",
        "students_desc",
        "program",
        "audience",
        "activity_type",
        "topic",
        'tag_relationship',
    ]
