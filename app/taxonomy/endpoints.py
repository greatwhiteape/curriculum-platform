from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Standard, StandardsBody, Program, Audience, Tag, Topic, AssetType, ActivityType, TimeEstimate


class ProgramsAPIEndpoint(BaseAPIEndpoint):
    model = Program

    body_fields = BaseAPIEndpoint.body_fields + [
        'program_name',
        'program_description',
        'program_url'
    ]

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
        'program_name',
        'program_description',
        'program_url'
    ]

class StandardAPIEndpoint(BaseAPIEndpoint):
    model = Standard

    body_fields = BaseAPIEndpoint.body_fields + [
        'standard',
        'standard_group',
        'standard_link',
        'description',
    ]

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
        'standard',
        'standard_group',
        'standard_link',
        'description',
    ]

class StandardsBodyAPIEndpoint(BaseAPIEndpoint):
    model = StandardsBody

    body_fields = BaseAPIEndpoint.body_fields + [
        'standards_body',
        'standards_body_url',
    ]

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
        'standards_body',
        'standards_body_url',
    ]

class AudienceAPIEndpoint(BaseAPIEndpoint):
    model = Audience

    body_fields = BaseAPIEndpoint.body_fields + [
        'age_range',
        'description',
    ]

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + [
        'age_range',
        'description',
    ]

class TagAPIEndpoint(BaseAPIEndpoint):
    model = Tag

    body_fields = BaseAPIEndpoint.body_fields + ['tag']

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['tag']

class TopicAPIEndpoint(BaseAPIEndpoint):
    model = Topic

    body_fields = BaseAPIEndpoint.body_fields + ['topic']

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['topic']

class AssetTypeAPIEndpoint(BaseAPIEndpoint):
    model = AssetType

    body_fields = BaseAPIEndpoint.body_fields + ['asset_type']

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['asset_type']

class ActivityTypeAPIEndpoint(BaseAPIEndpoint):
    model = ActivityType

    body_fields = BaseAPIEndpoint.body_fields + ['activity_type']

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['activity_type']

class TimeEstimateAPIEndpoint(BaseAPIEndpoint):
    model = TimeEstimate

    body_fields = BaseAPIEndpoint.body_fields + ['time_estimate']

    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['time_estimate']

