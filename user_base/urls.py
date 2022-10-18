from django.urls import path
from user_base import views
app_name = 'user_base'

urlpatterns = [
    path('list_user/',views.list_user , name = 'list_user' ),
    path('create_user/', views.create_user, name='create_user'),
    path('describe_user/', views.describe_user, name='describe_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('get_user_teams/', views.get_user_teams, name='get_user_teams'),

]