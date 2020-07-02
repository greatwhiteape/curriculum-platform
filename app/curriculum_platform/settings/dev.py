from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 't2e-puz@-va-he4f_d%37osu(03(fk3s6+hr(70p7jz!4$d6v*'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS += []

try:
    from .local import *
except ImportError:
    pass
