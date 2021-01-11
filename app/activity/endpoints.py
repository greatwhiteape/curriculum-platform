from wagtail.api.v2.views import BaseAPIViewSet

from .models import Activity


class ActivitiesAPIEndpoint(BaseAPIViewSet):
    model = Activity

    body_fields = BaseAPIViewSet.body_fields + [
        "live",
        'slug',
        "title",
        "overview_copy",
        "teachers_desc",
        "students_desc",
        "program",
        "audience_relationship",
        "activity_type",
        "topic",
        "tag_relationship",
        "learningspace_relationship",
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        "live",
        'slug',
        "title",
        "overview_copy",
        "teachers_desc",
        "students_desc",
        "program",
        "audience_relationship",
        "activity_type",
        "topic",
        "tag_relationship",
        "learningspace_relationship",
    ]
