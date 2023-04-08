from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from core.http import redirect_back
from core.auth.mixins import BaseLoginRequiredMixin

from common_users.constants import UserType
from common_users.models import Notice, CommonUser

from business_processes.models import BusinessProcessAsIs, BusinessProcessToBe
from business_processes.forms import (
    BusinessProcessAsIsModelForm,
    BusinessProcessAsIsChangeStatusModelForm,
    BusinessProcessToBeChangeStatusModelForm,
)
from business_processes.services.change_status_buttons import (
    get_action_buttons,
)


class BusinessProcessAsIsListView(BaseLoginRequiredMixin, ListView):
    """BusinessProcessAsIsListView"""

    model = BusinessProcessAsIs
    template_name = "pages/business_processes/as-is/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        is_can_add = False
        if self.request.user.user_type == UserType.BUSINESS_ANALYST:
            is_can_add = True
        context["is_can_add"] = is_can_add
        return context


class BusinessProcessToBeListView(BaseLoginRequiredMixin, ListView):
    """BusinessProcessToBeListView"""

    model = BusinessProcessToBe
    template_name = "pages/business_processes/to-be/list.html"

    def get_queryset(self):
        qs = (
            super()
            .get_queryset()
            .filter(business_process_as_is_id=self.kwargs.get("pk", None))
            .select_related("business_process_as_is", "author")
        )
        return qs


class BusinessProcessCreateView(BaseLoginRequiredMixin, CreateView):
    """CareerCreateView"""

    model = BusinessProcessAsIs
    template_name = "pages/business_processes/form.html"
    success_url = reverse_lazy("home")
    form_class = BusinessProcessAsIsModelForm

    def post(self, request, *args, **kwargs):
        data = request.POST
        form = self.form_class(data)

        if form.is_valid():
            business_process = form.save(commit=False)
            business_process.author = request.user
            business_process.save()
            success_url = reverse_lazy(
                "as_is_business_process_diagram",
                kwargs={"pk": business_process.id},
            )
            employees = CommonUser.objects.filter(user_type=UserType.EMPLOYEE)
            insert_data = []
            notice_title = _("Created a new business process")
            notice_text = _(
                f"{request.user.full_name} created a new business process: {business_process.title}"
            )
            for employee in employees:
                notice_data = Notice(
                    recipient=employee, title=notice_title, text=notice_text
                )
                insert_data.append(notice_data)

            Notice.objects.bulk_create(insert_data)
            return redirect_back(request, success_url)


class BusinessProcessUpdateView(BaseLoginRequiredMixin, UpdateView):
    """BusinessProcessUpdateView"""

    model = BusinessProcessAsIs
    template_name = "pages/business_processes/form.html"
    success_url = reverse_lazy("home")
    form_class = BusinessProcessAsIsModelForm


class BusinessProcessDiagramToBeTemplateView(
    BaseLoginRequiredMixin, TemplateView
):
    """BusinessProcessDiagramToBeTemplateView"""

    model = BusinessProcessToBe
    template_name = "pages/business_processes/diagram-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        business_process_to_be = BusinessProcessToBe.objects.filter(
            id=self.kwargs.get("pk", None)
        ).first()

        business_process_as_is = None

        if business_process_to_be:
            business_process_as_is = (
                business_process_to_be.business_process_as_is
            )

        to_be_buttons, as_is_buttons = get_action_buttons(
            to_be=business_process_to_be,
            as_is=business_process_as_is,
            user=user,
        )

        context["to_be_buttons"] = to_be_buttons
        context["as_is_buttons"] = as_is_buttons

        context["object_to_be"] = business_process_to_be
        context["object_as_is"] = business_process_as_is

        return context


class BusinessProcessAsIsDiagramTemplateView(
    BaseLoginRequiredMixin, TemplateView
):
    """BusinessProcessAsIsDiagramTemplateView"""

    model = BusinessProcessAsIs
    template_name = "pages/business_processes/diagram-view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        business_process_as_is = BusinessProcessAsIs.objects.filter(
            id=self.kwargs.get("pk", None)
        ).first()

        context["object_as_is"] = business_process_as_is

        business_process_to_be = BusinessProcessToBe.objects.filter(
            author=user,
            business_process_as_is_id=self.kwargs.get("pk", None),
        ).first()

        context["object_to_be"] = business_process_to_be

        to_be_buttons, as_is_buttons = get_action_buttons(
            to_be=business_process_to_be,
            as_is=business_process_as_is,
            user=user,
        )

        context["to_be_buttons"] = to_be_buttons
        context["as_is_buttons"] = as_is_buttons

        return context


class BusinessProcessAsIsDiagramEditTemplateView(
    BaseLoginRequiredMixin, TemplateView
):
    """BusinessProcessTemplateView"""

    model = BusinessProcessAsIs
    template_name = "pages/business_processes/diagram-form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["get_type"] = "as-is"
        context["update_type"] = "as-is"

        business_process = BusinessProcessAsIs.objects.filter(
            id=self.kwargs.get("pk", None)
        ).first()

        if business_process:
            context["object"] = business_process
            context["update_id"] = business_process.id
        return context


class BusinessProcessToBeDiagramEditTemplateView(
    BaseLoginRequiredMixin, TemplateView
):
    """BusinessProcessTemplateView"""

    model = BusinessProcessToBe
    template_name = "pages/business_processes/diagram-form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        (
            business_process_to_be,
            created,
        ) = BusinessProcessToBe.objects.get_or_create(
            author=self.request.user,
            business_process_as_is_id=self.kwargs.get("pk", None),
        )
        business_process_type = "as-is"
        business_process_object = business_process_to_be.business_process_as_is

        if business_process_to_be.data:
            business_process_type = "to-be"
            business_process_object = business_process_to_be

        context["get_type"] = business_process_type
        context["update_type"] = "to-be"
        context["update_id"] = business_process_to_be.id

        context["object"] = business_process_object

        return context


class BusinessProcessAsIsChangeStatusUpdateView(
    BaseLoginRequiredMixin, UpdateView
):
    """BusinessProcessToBeChangeStatusUpdateView"""

    model = BusinessProcessAsIs
    template_name = "pages/business_processes/form.html"
    form_class = BusinessProcessAsIsChangeStatusModelForm

    def get_success_url(self):
        return reverse_lazy(
            "as_is_business_process_diagram",
            kwargs={"pk": self.get_object().id},
        )


class BusinessProcessToBeChangeStatusUpdateView(
    BaseLoginRequiredMixin, UpdateView
):
    """BusinessProcessToBeChangeStatusUpdateView"""

    model = BusinessProcessToBe
    template_name = "pages/business_processes/form.html"
    form_class = BusinessProcessToBeChangeStatusModelForm

    def get_success_url(self):
        return reverse_lazy(
            "to_be_business_process_diagram",
            kwargs={"pk": self.get_object().id},
        )


class BusinessProcessAsIsDeleteView(BaseLoginRequiredMixin, DeleteView):
    """BusinessProcessAsIsDeleteView"""

    model = BusinessProcessAsIs
    success_url = reverse_lazy("home")
