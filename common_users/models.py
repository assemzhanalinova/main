from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from core.models.base import BaseUUIDModel

from common_users.constants import (
    UserType,
)
from common_users.managers import UserManager


class CommonUser(AbstractBaseUser, PermissionsMixin, BaseUUIDModel):
    """CommonUser"""

    email = models.EmailField(
        verbose_name=_("Email address"), blank=True, null=True, unique=True
    )
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="employees",
    )
    first_name = models.CharField(
        verbose_name=_("First name"), max_length=32, blank=True, default=""
    )
    user_type = models.PositiveSmallIntegerField(
        verbose_name=_("User type"),
        choices=UserType.CHOICES,
        default=UserType.EMPLOYEE,
    )
    last_name = models.CharField(
        verbose_name=_("Last name"), max_length=255, blank=True, default=""
    )
    birthday = models.DateField(
        verbose_name=_("Date of birthday"), null=True, blank=True
    )
    is_active = models.BooleanField(verbose_name=_("Is active"), default=True)
    is_staff = models.BooleanField(verbose_name=_("Is staff"), default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    USERTYPE_FIELD = "user_type"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("CommonUser")
        verbose_name_plural = _("CommonUsers")
        db_table = "common_users"

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"


class Notice(BaseUUIDModel):
    """Notice"""

    title = models.CharField(verbose_name=_("Title"), max_length=100)
    text = models.CharField(verbose_name=_("Text"), max_length=225)
    recipient = models.ForeignKey(
        CommonUser, related_name="notices", on_delete=models.CASCADE
    )
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Notice")
        verbose_name_plural = _("Notices")
        db_table = "notices"
