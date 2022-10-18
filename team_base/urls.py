from django.urls import path
from team_base import views

app_name = 'team_base'

urlpatterns = [
    path('list_team/',views.list_teams , name = 'list_team' ),
    path('update_team/', views.update_team, name='update_team'),
    path('list_team_users/', views.list_team_users, name='describe_user'),
    path('remove_users_from_team/', views.remove_users_from_team, name='remove_users_from_team'),
    path('add_users_to_team/', views.add_users_to_team, name='add_users_to_team'),
    path('describe_team/', views.describe_team, name='describe_team'),
    path('create_team/', views.create_team, name='create_team'),



]