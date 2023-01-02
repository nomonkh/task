from celery import shared_task
from .models import TaskModel, ErrorLogModels
import requests
from datetime import datetime


@shared_task(name='filtering_tasks')
def filtering_tasks():
    try:
        TaskModel.objects.filter(status=True).update(status_exist=True)
        print("well done")

    except Exception as e:
        error_type = type(e)
        error = str(error_type) + ' ' + str(e)
        error_time = datetime.now()

        error_to_db = ErrorLogModels(
            error_name=error,
            error_time=error_time,
            error_of_task='refresh_weather',
        )
        error_to_db.save()
        print("some thing is wrong")


