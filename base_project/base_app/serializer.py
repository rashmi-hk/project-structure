from rest_framework import serializers
from .models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    """
    CustomUser model serializer
    """

    class Meta:
        model = UserInfo
        fields = "__all__"

