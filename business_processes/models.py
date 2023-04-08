from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models.base import BaseUUIDModel

from business_processes.constants import (
    BusinessProcessAsIsStatus,
    BusinessProcessToBeStatus,
)


class BusinessProcessAsIs(BaseUUIDModel):
    """BusinessProcessAsIs"""

    title = models.CharField(
        max_length=100, verbose_name=_("Title"), null=True
    )
    author = models.ForeignKey(
        "common_users.CommonUser",
        verbose_name=_("Author"),
        related_name="business_processes",
        on_delete=models.CASCADE,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name=_("Status"),
        choices=BusinessProcessAsIsStatus.CHOICES,
        default=BusinessProcessAsIsStatus.DRAFT,
    )
    data = models.JSONField(verbose_name=_("Data"), null=True, blank=True)

    class Meta:
        verbose_name = _("Business process")
        verbose_name_plural = _("Business processes")
        db_table = "as_is_business_processes"


class BusinessProcessToBe(BaseUUIDModel):
    """BusinessProcessToBe"""

    business_process_as_is = models.ForeignKey(
        BusinessProcessAsIs,
        related_name="business_process_as_is",
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        "common_users.CommonUser",
        verbose_name=_("Author"),
        related_name="business_process_to_be",
        on_delete=models.CASCADE,
    )
    data = models.JSONField(verbose_name=_("Data"), null=True, blank=True)
    status = models.PositiveSmallIntegerField(
        verbose_name=_("Status"),
        choices=BusinessProcessToBeStatus.CHOICES,
        default=BusinessProcessToBeStatus.DRAFT,
    )

    class Meta:
        verbose_name = _("Business process")
        verbose_name_plural = _("Business processes")
        db_table = "to_be_business_processes"
