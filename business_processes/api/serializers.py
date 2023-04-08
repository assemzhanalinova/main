from rest_framework import serializers

from business_processes.models import BusinessProcessAsIs, BusinessProcessToBe


class BusinessProcessAsIsSerializer(serializers.ModelSerializer):
    """BusinessProcessAsIsSerializer"""

    class Meta:
        model = BusinessProcessAsIs
        fields = "__all__"


class BusinessProcessToBeSerializer(serializers.ModelSerializer):
    """BusinessProcessToBeSerializer"""

    class Meta:
        model = BusinessProcessToBe
        fields = "__all__"
