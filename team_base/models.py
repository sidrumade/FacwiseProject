from django.db import models
from user_base.models import UserBase
# Create your models here.

class TeamBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64, blank=False, default='')
    description = models.CharField(max_length=64, blank=False, default='', )
    creation_time = models.DateTimeField(auto_now_add=True)
    admin = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.name
