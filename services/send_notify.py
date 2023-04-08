from django.core.mail import send_mail
from django.conf import settings
from django.template import loader
from django.utils.html import strip_tags


def send_email_after_change_data(subject, html_data, email_list=None):
    """send email for users"""
    if email_list is None:
        email_list = []

    html_template = "email/base.html"

    html_message = loader.render_to_string(
        html_template,
        {
            "data": html_data,
        },
    )
    customer_plain_message = strip_tags(html_message)
    send_mail(
        subject=str(subject),
        message=customer_plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=email_list,
        html_message=html_message,
    )
