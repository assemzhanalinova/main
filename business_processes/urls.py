from django.urls import path

from business_processes.views import (
    BusinessProcessCreateView,
    BusinessProcessUpdateView,
    BusinessProcessAsIsListView,
    BusinessProcessToBeListView,
    BusinessProcessAsIsDiagramTemplateView,
    BusinessProcessAsIsDiagramEditTemplateView,
    BusinessProcessToBeDiagramEditTemplateView,
    BusinessProcessAsIsChangeStatusUpdateView,
    BusinessProcessToBeChangeStatusUpdateView,
    BusinessProcessDiagramToBeTemplateView,
    BusinessProcessAsIsDeleteView,
)

urlpatterns = [
    path("", BusinessProcessAsIsListView.as_view(), name="home"),
    path(
        "to-be/<pk>", BusinessProcessToBeListView.as_view(), name="to_be_list"
    ),
    path(
        "create",
        BusinessProcessCreateView.as_view(),
        name="business_process_create",
    ),
    path(
        "edit/<pk>",
        BusinessProcessUpdateView.as_view(),
        name="as_is_business_process_edit",
    ),
    path(
        "change_status/as-is/<pk>",
        BusinessProcessAsIsChangeStatusUpdateView.as_view(),
        name="as_is_business_process_change_status",
    ),
    path(
        "change_status/to-be/<pk>",
        BusinessProcessToBeChangeStatusUpdateView.as_view(),
        name="to_be_business_process_change_status",
    ),
    path(
        "diagram/to-be/<pk>",
        BusinessProcessDiagramToBeTemplateView.as_view(),
        name="to_be_business_process_diagram",
    ),
    path(
        "diagram/as-is/<pk>",
        BusinessProcessAsIsDiagramTemplateView.as_view(),
        name="as_is_business_process_diagram",
    ),
    path(
        "diagram/to-be/edit/<pk>",
        BusinessProcessToBeDiagramEditTemplateView.as_view(),
        name="to_be_business_process_diagram_edit",
    ),
    path(
        "diagram/as-is/edit/<pk>",
        BusinessProcessAsIsDiagramEditTemplateView.as_view(),
        name="as_is_business_process_diagram_edit",
    ),
    path(
        "diagram/as-is/delete/<pk>",
        BusinessProcessAsIsDeleteView.as_view(),
        name="as_is_business_process_diagram_delete",
    ),
]
