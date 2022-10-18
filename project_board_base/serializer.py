from project_board_base.models import ProjectBoardBase,Task
from rest_framework import serializers


class ProjectBoardBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBoardBase
        fields = ['id', 'name','team_id']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'description','user_id','creation_time','status']

