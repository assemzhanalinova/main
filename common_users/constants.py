from core.models.model_fields import BaseChoices


class UserType(BaseChoices):
    """UserType"""

    EMPLOYEE = 1
    SUPERVISOR = 2
    BUSINESS_ANALYST = 3
    SUPER_ADMIN = 4
    DIRECTOR = 5

    CHOICES = (
        (EMPLOYEE, "Employee"),
        (SUPERVISOR, "Supervisor"),
        (BUSINESS_ANALYST, "Business analyst"),
        (SUPER_ADMIN, "Super admin"),
        (DIRECTOR, "Director"),
    )
