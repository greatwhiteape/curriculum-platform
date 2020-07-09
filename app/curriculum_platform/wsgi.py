"""
WSGI config for curriculum_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings = "curriculum_platform.settings.{}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings.format(os.environ.get('CURRICULUM_ENV')))
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_platform.settings.dev")

application = get_wsgi_application()
