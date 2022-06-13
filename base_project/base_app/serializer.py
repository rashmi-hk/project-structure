from rest_framework import serializers
from .models import UserInfo, EmployeeInfo


class UserInfoSerializer(serializers.ModelSerializer):
    """
    CustomUser model serializer
    """

    class Meta:
        model = UserInfo
        fields = "__all__"


class EmployeeInfoSerializer(serializers.ModelSerializer):
    """
    EmployeeInfo model serializer
    """

    class Meta:
        model = EmployeeInfo
        fields = "__all__"
