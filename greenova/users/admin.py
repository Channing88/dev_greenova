from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Profile


class ProfileInline(admin.StackedInline):
    """Inline admin for user profiles."""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'


class UserAdmin(BaseUserAdmin):
    """Enhanced User admin with Profile inline."""
    inlines = (ProfileInline,)
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active'
    )


# Unregister the default User admin and register our enhanced version
admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserAdmin)
