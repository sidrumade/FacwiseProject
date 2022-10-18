from user_base.models import UserBase
from rest_framework import serializers


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = ['name', 'display_name', 'creation_time']

