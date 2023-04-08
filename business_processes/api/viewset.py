from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from rest_framework import generics, viewsets, status
from rest_framework.response import Response


from common_users.models import Notice

from business_processes.models import BusinessProcessAsIs, BusinessProcessToBe
from business_processes.api.serializers import (
    BusinessProcessAsIsSerializer,
    BusinessProcessToBeSerializer,
)


class BusinessProcessAsIsViewSet(
    generics.ListAPIView,
    generics.UpdateAPIView,
    generics.RetrieveAPIView,
    viewsets.GenericViewSet,
):
    """BusinessProcessAsIsViewSet"""

    queryset = BusinessProcessAsIs.objects.all()
    serializer_class = BusinessProcessAsIsSerializer

    def retrieve(self, request, *args, **kwargs):
        business_process = self.get_object()
        return_data = []
        if business_process.data:
            return_data = business_process.data
        return Response(return_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        data = request.data
        business_process = self.get_object()
        business_process.data = data
        business_process.save()
        return Response(data, status=status.HTTP_200_OK)


class BusinessProcessToBeViewSet(
    generics.ListAPIView,
    generics.UpdateAPIView,
    generics.RetrieveAPIView,
    viewsets.GenericViewSet,
):
    """BusinessProcessToBeViewSet"""

    queryset = BusinessProcessToBe.objects.select_related(
        "business_process_as_is", "business_process_as_is__author"
    )
    serializer_class = BusinessProcessToBeSerializer

    def retrieve(self, request, *args, **kwargs):
        business_process = self.get_object()
        return_data = []
        if business_process.data:
            return_data = business_process.data
        return Response(return_data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        data = request.data
        business_process = self.get_object()
        business_process.data = data
        business_process.save()
        business_process_as_is = business_process.business_process_as_is
        business_process_url = "http://localhost:8005/%s" % reverse_lazy(
            "to_be_business_process_diagram",
            kwargs={"pk": business_process.id},
        )

        html_data = {
            "business_process_name": business_process_as_is.title,
            "business_process_url": business_process_url,
            "user_full_name": self.request.user.full_name,
        }
        users_list = [
            business_process_as_is.author.email,
        ]
        if self.request.user.parent:
            users_list.append(self.request.user.parent.email)
        #
        # send_email_after_change_data(
        #     subject="Диаграмма была изменена",
        #     html_data=html_data,
        #     email_list=users_list,
        # )
        insert_data = []

        notice_title = _("Diagram has been changed")
        notice_text = _(
            f"Diagram has been changed by user: {self.request.user.full_name}"
        )

        for employee in [
            business_process_as_is.author,
            self.request.user.parent,
        ]:
            notice_data = Notice(
                recipient=employee, title=notice_title, text=notice_text
            )
            insert_data.append(notice_data)

        Notice.objects.bulk_create(insert_data)

        return Response(data, status=status.HTTP_200_OK)
