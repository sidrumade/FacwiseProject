from django.contrib import admin
from project_board_base.models import ProjectBoardBase,Task
# Register your models here.

admin.site.register(ProjectBoardBase)
admin.site.register(Task)