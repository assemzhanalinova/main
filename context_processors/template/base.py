from common_users.constants import UserType
from common_users.models import Notice


def template_variables(request):
    """returns project url name"""
    data = {
        "user_type": UserType,
    }

    if request.user.is_authenticated:
        notices = Notice.objects.filter(recipient=request.user, is_read=False)
        data["notices"] = notices
        data["notice_count"] = len(notices)

    return data
