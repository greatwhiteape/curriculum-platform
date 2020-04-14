from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Asset


class AssetsAPIEndpoint(BaseAPIEndpoint):
    model = Asset
    
    body_fields = BaseAPIEndpoint.body_fields + [
        'description',
        'internal_link',
        'external_link',
        'program',
        'asset_type',
        'student_asset',
        'audience',
    ]