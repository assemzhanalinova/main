from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.http import JsonResponse

from core.auth.mixins import BaseLoginRequiredMixin

from common_users.models import CommonUser, Notice


class EmployeeListView(BaseLoginRequiredMixin, ListView):
    """EmployeeListView"""

    model = CommonUser
    template_name = "pages/common_users/employees/list.html"

    def get_queryset(self):
        qs = super().get_queryset().filter(parent=self.request.user)
        return qs


class NoticeUpdateView(BaseLoginRequiredMixin, UpdateView):
    """NoticeUpdateView"""

    model = Notice
    fields = ["is_read"]
    success_url = None

    def post(self, request, *args, **kwargs):
        notice = self.get_object()
        notice.is_read = True
        notice.save()
        notices = Notice.objects.filter(recipient=request.user, is_read=False)
        data = {"notice_count": notices.count()}
        return JsonResponse(data, status=200)
