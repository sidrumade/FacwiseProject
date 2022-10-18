from team_base.models import TeamBase
from rest_framework import serializers


class TeamBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamBase
        fields = ['id','name', 'description', 'creation_time','admin']



