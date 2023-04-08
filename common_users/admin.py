from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from common_users.models import CommonUser


@admin.register(CommonUser)
class CommonUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        "email",
        "first_name",
        "last_name",
        "user_type",
        "is_staff",
    )
    search_fields = ("email",)
    ordering = ["email"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "user_type",
                    "birthday",
                    "parent",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "user_type",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
