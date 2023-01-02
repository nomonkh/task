import uuid
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django_currentuser.db.models import CurrentUserField
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
    first_name = models.CharField(max_length=512, verbose_name='Исми', null=False)
    second_name = models.CharField(max_length=512, verbose_name='Фамилияси', null=False)
    third_name = models.CharField(max_length=255, verbose_name='Отасиниг исми', null=False)
    phone = models.CharField(max_length=255, verbose_name='Телефон рақами', null=False)
    sector = models.IntegerField(verbose_name='Сектор', choices=_sector, null=False)
    author = CurrentUserField(verbose_name='Муаллиф')

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.second_name, self.third_name)

    class Meta:
        verbose_name = 'Ижрочи'
        verbose_name_plural = 'Ижрочилар'
        managed = True
        db_table = 'task_users'


def upload_location(instance, filename):
    ext = filename.split('.')
    file_path = "{filename}".format(
        filename='{}_{}.{}'.format(instance.executor, ext[0], ext[-1]))
    return file_path


class TaskModel(models.Model):
    time_taken = models.DateField(verbose_name='Вазифа қабул қилиш санаси', null=False)
    time_started = models.DateTimeField(verbose_name='Вазифа яратилиш санаси', auto_now=True, blank=True)
    time_finished = models.DateTimeField(verbose_name='Вазифа тугатиш санаси', null=True, default=None, blank=True)
    time_of_day = models.CharField(max_length=255, verbose_name='Амалга ошириш вақти', choices=TIME_CHOICES, null=False)
    name_of_task = models.TextField(null=False,verbose_name='Вазифа номи')
    status = models.BooleanField(default=False, null=False,verbose_name='Холати')
    confirmation = models.FileField(upload_to=upload_location, null=True, blank=True,verbose_name='Тасдиқлаш файли')
    executor = models.ForeignKey('ExecutorModel', on_delete=models.CASCADE, null=False,verbose_name='Ижрочи')
    day_of_week = models.CharField(max_length=55, null=True, blank=True,verbose_name='Хафта куни')
    status_exist = models.BooleanField(default=False, null=False)
    author = CurrentUserField(verbose_name='Муаллиф')

    def __str__(self):
        return str(self.name_of_task)

    class Meta:
        verbose_name = 'Вазифа'
        verbose_name_plural = 'Вазифалар'
        managed = True
        db_table = 'task_model'


@receiver(pre_save, sender=TaskModel)
def file_check(sender, instance=None, created=False, **kwargs):
    if instance.confirmation:
        instance.status = True
        instance.time_finished = date()


class ErrorLogModels(models.Model):
    error_name = models.TextField(blank=True, null=True)
    error_time = models.DateTimeField()
    error_of_task = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{str(self.error_of_task)}-{str(self.error_name)}-{str(self.error_time)}"


