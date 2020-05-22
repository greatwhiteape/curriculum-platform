from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4)
    gmri_uuid = models.CharField(max_length=255, null=True, blank=True, unique=True)

    has_cas_connection = models.BooleanField(default=False)
