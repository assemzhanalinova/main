from django import forms

from core.forms.base import BaseInputCssStype

from business_processes.models import BusinessProcessAsIs, BusinessProcessToBe


class BusinessProcessAsIsModelForm(forms.ModelForm, BaseInputCssStype):
    """BusinessProcessAsIsModelForm"""

    class Meta:
        model = BusinessProcessAsIs
        fields = [
            "title",
        ]


class BusinessProcessAsIsChangeStatusModelForm(
    forms.ModelForm, BaseInputCssStype
):
    """BusinessProcessAsIsChangeStatusModelForm"""

    class Meta:
        model = BusinessProcessAsIs
        fields = [
            "status",
        ]


class BusinessProcessToBeChangeStatusModelForm(
    forms.ModelForm, BaseInputCssStype
):
    """BusinessProcessToBeChangeStatusModelForm"""

    class Meta:
        model = BusinessProcessToBe
        fields = [
            "status",
        ]
