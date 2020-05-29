from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class UserQuerySet(models.QuerySet):
    def cas_users(self):
        return self.exclude(gmri_uuid=None)


class GMRIUserManager(UserManager):
    def get_queryset(self):
        return UserQuerySet(self.model, using=self._db)

    def cas_users(self):
        return self.get_queryset().cas_users()


class User(AbstractUser):
    # id = models.UUIDField(primary_key=True, default=uuid4)
    gmri_uuid = models.CharField(max_length=255, null=True, blank=True, unique=True)

    has_cas_connection = models.BooleanField(default=False)
    objects = GMRIUserManager()

    @property
    def name(self):
        if self.first_name:
            return self.first_name
        return self.username.split("@")[0]

    @property
    def can_log_in_without_cas(self):
        """
        If the CAS is not available, then only users with local passwords
        would be able to log in.
        """
        return self.password is not None and self.password != ""
