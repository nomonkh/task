# Generated by Django 3.2.14 on 2023-01-02 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user_name',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='Фойдаланувчи номи'),
        ),
    ]
