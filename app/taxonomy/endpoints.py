from wagtail.api.v2.endpoints import BaseAPIEndpoint

from .models import Program


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
