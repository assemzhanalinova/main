from core.models.model_fields import BaseChoices


class BusinessProcessAsIsStatus(BaseChoices):
    """BusinessProcessAsIsStatus"""

    DRAFT = 1
    ACTIVE = 2
    COMPLETED = 3

    CHOICES = (
        (DRAFT, "Draft"),
        (ACTIVE, "Active"),
        (COMPLETED, "Competed"),
    )


class BusinessProcessToBeStatus(BaseChoices):
    """BusinessProcessToBeStatus"""

    DRAFT = 1
    REVIEW = 2
    APPROVED = 3
    NOT_APPROVED = 4
    AGREED = 5
    NOT_AGREED = 6

    CHOICES = (
        (DRAFT, "Draft"),
        (REVIEW, "Review"),
        (APPROVED, "Approved"),
        (NOT_APPROVED, "Not approved"),
        (AGREED, "Agreed"),
        (NOT_AGREED, "Not agreed"),
    )
