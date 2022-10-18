from django.db import models
from django.utils import  timezone
from django.utils.translation import gettext_lazy as ___
# Create your models here.

class ProjectBoardBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64, blank=False, default='')
    description = models.CharField(max_length=64, blank=False, default='' )
    creation_time = models.DateTimeField(blank=False,null=False,default=timezone.now)
    team_id = models.IntegerField(blank=False,null=False,default=0)
    class Board_StatusOps(models.TextChoices):
        OPEN = 'OPEN', ___('Open')
        CLOSE = 'CLOSE', ___('Close')

    status = models.CharField(
        max_length=5,
        choices=Board_StatusOps.choices,
        default=Board_StatusOps.OPEN,
    )

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=64, blank=False, default='')
    description = models.CharField(max_length=128, blank=False, default='', )
    user_id = models.IntegerField(blank=False,null=False,default=0)
    creation_time = models.DateTimeField(default=timezone.now,blank=False,null=False)
    class Task_StatusOps(models.TextChoices):
        OPEN = 'OPEN', ___('Open')
        IN_PROGRESS = 'IN_PROGRESS', ___('In_Progress')
        COMPLETE = 'COMPLETE', ___('Complete')

    status = models.CharField(
        max_length=12,
        choices=Task_StatusOps.choices,
        default=Task_StatusOps.OPEN,
    )


    def __str__(self):
        return self.title
