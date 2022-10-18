from django.urls import path
from project_board_base import views

app_name = 'project_board_base'

urlpatterns = [
    path('list_boards/',views.list_boards , name = 'list_boards' ),
    path('create_board/', views.create_board, name='update_team'),
    path('add_task/', views.add_task, name='add_task'),
    path('update_task_status/', views.update_task_status, name='update_task_status'),
    path('close_board/', views.close_board, name='close_board'),
    path('export_board/', views.export_board, name='export_board'),

]