from django.contrib import admin
from .models import TaskModel, ExecutorModel


admin.site.register(ExecutorModel)


@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    model = TaskModel
    list_display = [
        'time_taken',
        'time_of_day',
        'name_of_task',
        'status',
        'executor'
    ]
    exclude = (
        'time_finished',
        'time_started'
    )

