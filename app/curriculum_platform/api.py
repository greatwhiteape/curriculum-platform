from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

from activity.endpoints import ActivitiesAPIEndpoint
from assets.endpoints import AssetsAPIEndpoint
from lessons.endpoints import LessonsAPIEndpoint
from modules.endpoints import ModulesAPIEndpoint
from taxonomy.endpoints import ProgramsAPIEndpoint

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)

# Custom API Endpoints
api_router.register_endpoint('activities', ActivitiesAPIEndpoint)
api_router.register_endpoint('assets', AssetsAPIEndpoint)
api_router.register_endpoint('lessons', LessonsAPIEndpoint)
api_router.register_endpoint('modules', ModulesAPIEndpoint)
api_router.register_endpoint('programs', ProgramsAPIEndpoint)
