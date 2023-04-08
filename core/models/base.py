import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from core.utils.translate_name import get_translation_dict_by_choices


class BaseModel(models.Model):
    """BaseModel"""

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def _delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    @staticmethod
    def get_choice_object(object_id, choices):
        if object_id or isinstance(object_id, int):
            return get_translation_dict_by_choices(object_id, choices)
        return None


class BaseUUIDModel(BaseModel):
    """BaseUUIDModel"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    class Meta:
        abstract = True


class BaseNameModel(BaseUUIDModel):
    """BaseNameModel"""

    name = models.CharField(
        _("Name"), max_length=256, db_index=True, unique=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BaseNameTextModel(BaseNameModel):
    """BaseNameDescModel"""

    text = models.TextField(verbose_name=_("Text"), default="")

    class Meta:
        abstract = True


class BaseStartEndDateModel(BaseUUIDModel):
    """BaseStartEndDateModel"""

    start = models.DateTimeField(verbose_name=_("Start date"), default=now)
    end = models.DateTimeField(verbose_name=_("End date"), default=now)

    class Meta:
        abstract = True


class BaseScheduleModel(BaseStartEndDateModel):
    """BaseScheduleModel"""

    is_full_day = models.BooleanField(
        verbose_name=_("Is full day"), default=False
    )

    class Meta:
        abstract = True
