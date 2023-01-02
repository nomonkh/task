from django.urls import path
from .views import *

app_name = 'job_app'


urlpatterns = [
    path('monday', task_view_monday, name='task_monday'),
    path('tuesday', task_view_tuesday, name='task_tuesday'),
    path('wednesday', task_view_wednesday, name='task_wednesday'),
    path('thursday', task_view_thursday, name='task_thursday'),
    path('friday', task_view_friday, name='task_friday'),
    path('saturday', task_view_saturday, name='task_saturday'),
    path('create_task', create_task, name='add_task'),
    path('create_executor', create_executor, name='create_executor'),
    path('executors', executors_view, name='executors_view'),
    path('delete/<int:pk>', del_user, name='del_user'),
    path('update/<int:pk>', update_executor, name='update_executor'),
    path('update_task/<int:pk>', update_task, name='update_task'),
]




