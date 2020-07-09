from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from .models import User
from .utils import cas


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    actions = ["update_user_details"]

    def update_user_details(self, request, queryset):
        usernames = []

        for user in queryset.iterator():
            cas.update_user(user.username)

            usernames.append(user.username)

        message = "Updating user details for "

        if len(usernames) < 2:
            message += f"selected user: {usernames[0]}"
        else:
            message += f"selected users: {', '.join(usernames)}"

        self.message_user(request, message)

    update_user_details.short_description = "Update details from CAS"
