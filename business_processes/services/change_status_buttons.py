from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from pydantic import BaseModel

from common_users.constants import UserType

from business_processes.constants import (
    BusinessProcessToBeStatus,
    BusinessProcessAsIsStatus,
)


class ButtonType:
    BUTTON = 1
    LINK = 2


class ActionButton(BaseModel):
    """ActionButton"""

    title: str
    value: str
    css_class: str
    button_type: int


def generate_html_button(button_data, form_name):
    """

    :param button_data: ActionButton class
    :type button_data: dataclass

    :param form_name: template form name
    :type form_name: str

    :return: str
    """
    if button_data.button_type == ButtonType.BUTTON:
        html_button = (
            "<button type='submit' name='status' value='%s' form='%s' class='btn %s'>%s</button>"
            % (
                button_data.value,
                form_name,
                button_data.css_class,
                button_data.title,
            )
        )
    else:
        html_button = (
            "<a class='btn waves-effect waves-float waves-light %s' href='%s'>%s</a>"
            % (button_data.css_class, button_data.value, button_data.title)
        )
    return html_button


def get_to_be_buttons(to_be, as_is, user):
    """

    :param to_be: BusinessProcessToBe object
    :type to_be: model

    :param user: CommonUser object
    :type user: model

    :param as_is: BusinessProcessAsIs object
    :type as_is: model

    :return:
    """
    button_list = []

    if as_is is None:
        return button_list

    if as_is.status == BusinessProcessAsIsStatus.ACTIVE:
        if to_be is None and user.user_type == UserType.EMPLOYEE:
            button = ActionButton(
                title=str(_("Add To Be diagram")),
                value=str(
                    reverse_lazy(
                        "to_be_business_process_diagram_edit",
                        kwargs={"pk": as_is.id},
                    )
                ),
                css_class="btn-primary",
                button_type=ButtonType.LINK,
            )
            button_list.append(button)

        elif to_be and to_be.author == user:
            if to_be.status == BusinessProcessToBeStatus.DRAFT:
                button = ActionButton(
                    title=str(_("Review")),
                    value=str(BusinessProcessToBeStatus.REVIEW),
                    css_class="btn-info",
                    button_type=ButtonType.BUTTON,
                )
                button_list.append(button)

            elif to_be.status == BusinessProcessToBeStatus.REVIEW:
                button = ActionButton(
                    title=str(_("Review")),
                    value=str(BusinessProcessToBeStatus.DRAFT),
                    css_class="btn-danger",
                    button_type=ButtonType.BUTTON,
                )
                button_list.append(button)

            button = ActionButton(
                title=str(_("Edit To Be diagram")),
                value=str(
                    reverse_lazy(
                        "to_be_business_process_diagram_edit",
                        kwargs={"pk": as_is.id},
                    )
                ),
                css_class="btn-primary",
                button_type=ButtonType.LINK,
            )
            button_list.append(button)

        elif to_be:
            if (
                to_be.author.parent == user
                and user.user_type == UserType.SUPERVISOR
            ) or user.user_type == UserType.DIRECTOR:
                if to_be.status == BusinessProcessToBeStatus.REVIEW:
                    button = ActionButton(
                        title=str(_("Not approved")),
                        value=str(BusinessProcessToBeStatus.NOT_APPROVED),
                        css_class="btn-danger",
                        button_type=ButtonType.BUTTON,
                    )
                    button_list.append(button)

                    button = ActionButton(
                        title=str(_("Approved")),
                        value=str(BusinessProcessToBeStatus.APPROVED),
                        css_class="btn-success",
                        button_type=ButtonType.BUTTON,
                    )
                    button_list.append(button)

        elif (
            to_be
            and as_is.author == user
            and to_be.status == BusinessProcessToBeStatus.APPROVED
        ):
            button = ActionButton(
                title=str(_("Not agreed")),
                value=str(BusinessProcessToBeStatus.NOT_AGREED),
                css_class="btn-danger",
                button_type=ButtonType.BUTTON,
            )
            button_list.append(button)

            button = ActionButton(
                title=str(_("Agreed")),
                value=str(BusinessProcessToBeStatus.AGREED),
                css_class="btn-success",
                button_type=ButtonType.BUTTON,
            )
            button_list.append(button)

    new_button_list = []

    form_name = "to_be_change_status"

    for button_info in button_list:
        html_button = generate_html_button(button_info, form_name)
        new_button_list.append(html_button)

    return new_button_list


def get_as_is_buttons(as_is, user):
    """
    returns as is action buttons

    :param as_is: BusinessProcessAsIs object
    :type as_is: model

    :param user: CommonUser object
    :type user: model

    :return: list
    """

    button_list = []

    if as_is.author == user:
        if as_is.status == BusinessProcessAsIsStatus.DRAFT:
            button = ActionButton(
                title=str(_("Active")),
                value=str(BusinessProcessAsIsStatus.ACTIVE),
                css_class="btn-info",
                button_type=ButtonType.BUTTON,
            )
            button_list.append(button)
            button = ActionButton(
                title=str(_("Edit As Is diagram")),
                value=str(
                    reverse_lazy(
                        "as_is_business_process_diagram_edit",
                        kwargs={"pk": as_is.id},
                    )
                ),
                css_class="btn-primary",
                button_type=ButtonType.LINK,
            )
            button_list.append(button)

        elif as_is.status == BusinessProcessAsIsStatus.ACTIVE:
            button = ActionButton(
                title=str(_("Completed")),
                value=str(BusinessProcessAsIsStatus.COMPLETED),
                css_class="btn-success",
                button_type=ButtonType.BUTTON,
            )
            button_list.append(button)

    new_button_list = []

    form_name = "as_is_change_status"

    for button_info in button_list:
        html_button = generate_html_button(button_info, form_name)
        new_button_list.append(html_button)

    return new_button_list


def get_action_buttons(to_be, as_is, user):
    """
    returns action buttons
    :param to_be: BusinessProcessToBe object
    :type to_be: model

    :param as_is: BusinessProcessAsIs object
    :type to_be: model

    :param user: CommonUser object
    :type user: model

    :return: list
    """

    to_be_buttons_list = get_to_be_buttons(to_be, as_is, user)

    as_is_buttons_list = get_as_is_buttons(as_is, user)

    return to_be_buttons_list, as_is_buttons_list
