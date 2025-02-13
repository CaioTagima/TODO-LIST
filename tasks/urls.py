from django.urls import path
from . import views

from django.urls import path
from .views import task_list, rem_task, search_task, edit_task, migrate_task

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('tasks/delete/<int:task_id>/', rem_task, name='delete-task'),
    path('tasks/search/<str:task_title>/', search_task, name='search-task'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit-task'),
    path('tasks/migrate/<int:task_id>/', migrate_task, name='migrate-task'),
]