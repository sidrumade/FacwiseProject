from django.db import models


# Create your models here.

class UserBase(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=64, blank=False, default='')
    display_name = models.CharField(max_length=64, blank=False, default='', )
    creation_time = models.DateTimeField(auto_now_add=True)
    # team = models.ForeignKey(TeamBase, related_name='team', null=True, blank=True, on_delete=models.DO_NOTHING)

    team = models.ForeignKey('team_base.TeamBase',to_field='name',related_name='team', null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.name)
