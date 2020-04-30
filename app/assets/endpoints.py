from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Asset


class AssetsAPIEndpoint(BaseAPIEndpoint):
    model = Asset

    body_fields = BaseAPIEndpoint.body_fields + [
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

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
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
