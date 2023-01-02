from django import template
from job_app.models import TaskModel, TIME_CHOICES
import calendar

register = template.Library()


@register.simple_tag()
def get_data_monday():
    tasks = TaskModel.objects.all().values()
    for each in tasks:
        a = calendar.day_name[each['time_taken'].weekday()]
        if a == "Monday":
            TaskModel.objects.filter(time_taken=each['time_taken']).update(day_of_week=a)
    data = TaskModel.objects.filter(day_of_week='Monday').filter(status_exist=False)
    return data


@register.simple_tag()
def get_data_tuesday():
    tasks = TaskModel.objects.all().values()
    for each in tasks:
        a = calendar.day_name[each['time_taken'].weekday()]
        if a == "Tuesday":
            TaskModel.objects.filter(time_taken=each['time_taken']).update(day_of_week=a)
    data = TaskModel.objects.filter(day_of_week='Tuesday').filter(status_exist=False)
    return data


@register.simple_tag()
def get_data_wednesday():
    tasks = TaskModel.objects.all().values()
    for each in tasks:
        a = calendar.day_name[each['time_taken'].weekday()]
        if a == "Wednesday":
            TaskModel.objects.filter(time_taken=each['time_taken']).update(day_of_week=a)
    data = TaskModel.objects.filter(day_of_week='Wednesday').filter(status_exist=False)
    return data


@register.simple_tag()
def get_data_thursday():
    tasks = TaskModel.objects.all().values()
    for each in tasks:
        a = calendar.day_name[each['time_taken'].weekday()]
        if a == "Thursday":
            TaskModel.objects.filter(time_taken=each['time_taken']).update(day_of_week=a)
    data = TaskModel.objects.filter(day_of_week='Thursday').filter(status_exist=False)
    return data


@register.simple_tag()
def get_data_friday():
    tasks = TaskModel.objects.filter(status_exist=False).values()
    for each in tasks:
        a = calendar.day_name[each['time_taken'].weekday()]
        if a == "Friday":
            TaskModel.objects.filter(time_taken=each['time_taken']).update(day_of_week=a)
    data = TaskModel.objects.filter(day_of_week='Friday').filter(status_exist=False)
    return data


@register.simple_tag()
def get_data_saturday():
    obj = []
    tasks = TaskModel.objects.all().values()
    for each in tasks:
        a = calendar.day_name[each['time_taken'].weekday()]
        if a == "Saturday":
            TaskModel.objects.filter(time_taken=each['time_taken']).update(day_of_week=a)
    data = TaskModel.objects.filter(day_of_week='Saturday').filter(status_exist=False)
    return data



# @register.simple_tag()
# def get_data_sunday():
#     tasks = TaskModel.objects.all().values()
#     for each in tasks:
#         # a = calendar.day_name[each['time_taken'].weekday()]
#         # if a == "Sunday":
#         #     task = TaskModel.objects.filter(id=each['id'])
#         return tasks

