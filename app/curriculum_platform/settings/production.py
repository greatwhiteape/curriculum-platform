from .base import *

DEBUG = False
ALLOWED_HOSTS = ['teach.gmri.org']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *
except ImportError:
    pass
