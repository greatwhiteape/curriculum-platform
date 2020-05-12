from wagtail.api.v2.views import BaseAPIViewSet

from .models import Asset


class AssetsAPIEndpoint(BaseAPIViewSet):
    model = Asset

    body_fields = BaseAPIViewSet.body_fields + [
        'title',
        'description',
        'asset_link',
        'program',
        'asset_type',
        'student_asset',
        'program',
        'time_estimate',
        'audience_relationship',
        'standards_relationship',
        'topic_relationship',
        'tag_relationship',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        'title',
        'description',
        'asset_link',
        'program',
        'asset_type',
        'student_asset',
        'program',
        'time_estimate',
        'audience_relationship',
        'standards_relationship',
        'topic_relationship',
        'tag_relationship',
    ]
