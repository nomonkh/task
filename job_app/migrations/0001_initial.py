# Generated by Django 3.2.14 on 2023-01-02 07:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware
import job_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExecutorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=512, verbose_name='Исми')),
                ('second_name', models.CharField(max_length=512, verbose_name='Фамилияси')),
                ('third_name', models.CharField(max_length=255, verbose_name='Отасиниг исми')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон рақами')),
                ('sector', models.IntegerField(choices=[(1, 'первый'), (2, 'второй'), (3, 'третий'), (4, 'четвертый')], verbose_name='Сектор')),
                ('author', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Муаллиф')),
            ],
            options={
                'verbose_name': 'Ижрочи',
                'verbose_name_plural': 'Ижрочилар',
                'db_table': 'task_users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_taken', models.DateField(verbose_name='Вазифа қабул қилиш санаси')),
                ('time_started', models.DateTimeField(auto_now=True, verbose_name='Вазифа яратилиш санаси')),
                ('time_finished', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Вазифа тугатиш санаси')),
                ('time_of_day', models.CharField(choices=[('09:00-10:00', '09:00-10:00'), ('10:00-11:00', '10:00-11:00'), ('11:00-12:30', '11:00-12:30'), ('14:00-15:30', '14:00-15:30'), ('16:00-17:00', '16:00-17:00'), ('17:00-18:00', '17:00-18:00')], max_length=255, verbose_name='Амалга ошириш вақти')),
                ('name_of_task', models.TextField(verbose_name='Вазифа номи')),
                ('status', models.BooleanField(default=False, verbose_name='Холати')),
                ('confirmation', models.FileField(blank=True, null=True, upload_to=job_app.models.upload_location, verbose_name='Тасдиқлаш файли')),
                ('day_of_week', models.CharField(blank=True, max_length=55, null=True, verbose_name='Хафта куни')),
                ('author', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Муаллиф')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_app.executormodel', verbose_name='Ижрочи')),
            ],
            options={
                'verbose_name': 'Вазифа',
                'verbose_name_plural': 'Вазифалар',
                'db_table': 'task_model',
                'managed': True,
            },
        ),
    ]
