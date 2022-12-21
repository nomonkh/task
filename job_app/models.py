import os
import uuid

from django.db import models

_uuid = uuid.uuid1()


def date():
    from datetime import datetime
    now = datetime.now()
    return now


_date = date()
DAY_CHOICES = [
    ('Понедельник', 'Понедельник'),
    ('Вторник', 'Вторник'),
    ('Среда', 'Среда'),
    ('Четверг', 'Четверг'),
    ('Пятница', 'Пятница'),
    ('Суббота', 'Суббота')
]

TIME_CHOICES = [
    ('09:00-10:00', '09:00-10:00'),
    ('10:00-11:00', '10:00-11:00'),
    ('11:00-12:30', '11:00-12:30'),
    ('14:00-15:30', '14:00-15:30'),
    ('16:00-17:00', '16:00-17:00'),
    ('17:00-18:00', '17:00-18:00')
]


class ExecutorModel(models.Model):
    _sector = (
        (1, 'первый'),
        (2, 'второй'),
        (3, 'третий'),
        (4, 'четвертый'),
    )
    first_name = models.CharField(max_length=512, verbose_name='Имя', null=False)
    second_name = models.CharField(max_length=512, verbose_name='Фамилия', null=False)
    third_name = models.CharField(max_length=255, verbose_name='Отчество', null=False)
    phone = models.CharField(max_length=255, verbose_name='Номер телефона', null=False)
    sector = models.IntegerField(verbose_name='Сектор', choices=_sector, null=False)

    def __str__(self):
        return '{} {} {} {}'.format(self.first_name, self.second_name, self.third_name, self.sector)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'
        managed = True
        db_table = 'task_users'


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    title = f'{instance.executor_id}_{_uuid}'
    file_path = "executor_conf/{filename}".format(
        filename='{}.{}'.format(title, ext))
    return file_path


class TaskModel(models.Model):
    time_taken = models.DateField(verbose_name='Дата принятия задачи', null=False)
    time_started = models.DateTimeField(verbose_name='Дата создания задачи', auto_now=True, blank=True)
    time_finished = models.DateTimeField(verbose_name='Дата закрытия задачи', null=True, default=None, blank=True)
    time_of_day = models.CharField(max_length=255, verbose_name='Время исполнение', choices=TIME_CHOICES, null=False)
    name_of_task = models.TextField(null=False)
    status = models.BooleanField(default=False, null=False)
    confirmation = models.FileField(upload_to=upload_location, null=True, blank=True)
    executor = models.ForeignKey('ExecutorModel', on_delete=models.CASCADE, null=False)

    def save(self, *args, **kwargs):
        if self.status:
            self.time_finished = date()
        super(TaskModel, self).save(*args, **kwargs)

    def __str__(self):
        return '{} {} {} {}'.format(self.time_taken, self.time_of_day, self.name_of_task, self.status)

    class Meta:
        verbose_name = 'Задач'
        verbose_name_plural = 'Задачи'
        managed = True
        db_table = 'task_model'
