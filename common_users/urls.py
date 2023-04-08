from django.urls import path

from common_users.views import EmployeeListView, NoticeUpdateView

urlpatterns = [
    path("employees", EmployeeListView.as_view(), name="employees"),
    path("notice/<pk>", NoticeUpdateView.as_view(), name="notice_update"),
]
