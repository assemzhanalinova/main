from django import forms
from django.forms.widgets import Textarea, Select
from django.utils.translation import get_language
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class BaseInputCssStype(forms.BaseForm):
    """BaseInputCssStype"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        current_language = get_language()

        for visible in self.visible_fields():
            widget = visible.field.widget
            if (
                not isinstance(widget, Textarea)
                and widget.input_type == "text"
                and hasattr(widget, "picker_type")
                and (
                    (
                        widget.picker_type == "DATE"
                        and widget.format_key == "DATE_INPUT_FORMATS"
                    )
                    or (
                        widget.picker_type == "DATETIME"
                        and widget.format_key == "DATETIME_INPUT_FORMATS"
                    )
                )
            ):
                options = widget.config.options
                options.locale = current_language

            if not isinstance(widget, Textarea):
                if widget.input_type == "checkbox":
                    widget.attrs["class"] = "form-check-input"
                else:
                    widget.attrs["class"] = "form-control"
            else:
                widget.attrs["class"] = "form-control"

            if isinstance(widget, Select) and hasattr(widget, "choices"):
                translate_choices = [(x[0], _(x[1])) for x in widget.choices]
                widget.choices = translate_choices


class BaseLoginForm(AuthenticationForm, BaseInputCssStype):
    """BaseLoginForm"""

    def clean(self):
        """
        close access for authorizations
        to a user with the user_type = CLIENT
        """
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
