from django.contrib import admin
from .models import TaskModel, ExecutorModel


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_taken', 'time_of_day', 'status', 'executor', 'author')
    list_display_links = ('id',)
    search_fields = ('id', )
    list_filter = ('id',)
    exclude = ('time_finished', 'day_of_week')


admin.site.register(TaskModel, TasksAdmin)


class ExecutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name', 'third_name', 'phone', 'sector', 'author')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'second_name', 'phone')
    list_filter = ('id', )
    # exclude = ('time_finished', 'time_started')


admin.site.register(ExecutorModel, ExecutorAdmin)