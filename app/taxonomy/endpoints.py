from wagtail.api.v2.views import BaseAPIViewSet

from .models import Standard, StandardsBody, Program, Audience, Tag, Topic, AssetType, ActivityType, TimeEstimate, LearningSpace


class ProgramsAPIEndpoint(BaseAPIViewSet):
    model = Program

    body_fields = BaseAPIViewSet.body_fields + [
        'program_name',
        'program_description',
        'program_url',
        'program_color'
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        'program_name',
        'program_description',
        'program_url',
        'program_color'
    ]

class StandardAPIEndpoint(BaseAPIViewSet):
    model = Standard

    body_fields = BaseAPIViewSet.body_fields + [
        'standard',
        'standard_group',
        'standard_link',
        'description',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        'standard',
        'standard_group',
        'standard_link',
        'description',
    ]

class StandardsBodyAPIEndpoint(BaseAPIViewSet):
    model = StandardsBody

    body_fields = BaseAPIViewSet.body_fields + [
        'standards_body',
        'standards_body_url',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        'standards_body',
        'standards_body_url',
    ]

class AudienceAPIEndpoint(BaseAPIViewSet):
    model = Audience

    body_fields = BaseAPIViewSet.body_fields + [
        'age_range',
        'description',
    ]

    listing_default_fields = BaseAPIViewSet.listing_default_fields + [
        'age_range',
        'description',
    ]

class TagAPIEndpoint(BaseAPIViewSet):
    model = Tag

    body_fields = BaseAPIViewSet.body_fields + ['tag']

    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['tag']

class TopicAPIEndpoint(BaseAPIViewSet):
    model = Topic

    body_fields = BaseAPIViewSet.body_fields + ['topic']

    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['topic']

class AssetTypeAPIEndpoint(BaseAPIViewSet):
    model = AssetType

    body_fields = BaseAPIViewSet.body_fields + ['asset_type']

    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['asset_type']

class ActivityTypeAPIEndpoint(BaseAPIViewSet):
    model = ActivityType

    body_fields = BaseAPIViewSet.body_fields + ['activity_type']

    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['activity_type']

class TimeEstimateAPIEndpoint(BaseAPIViewSet):
    model = TimeEstimate

    body_fields = BaseAPIViewSet.body_fields + ['time_estimate']

    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['time_estimate']

class LearningSpaceAPIEndpoint(BaseAPIViewSet):
    model = LearningSpace

    body_fields = BaseAPIViewSet.body_fields + ['learning_space']

    listing_default_fields = BaseAPIViewSet.listing_default_fields + ['learning_space']
