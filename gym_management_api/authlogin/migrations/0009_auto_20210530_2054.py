# Generated by Django 3.2 on 2021-05-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authlogin', '0008_alter_userprofiles_last_login_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='is_gym_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofiles',
            name='staff_role',
            field=models.CharField(choices=[('TRAINER', 'TRAINER'), ('PTRAINER', 'PTRAINER'), ('ACCOUNTANT', 'ACCOUNTANT'), ('CLEANING', 'CLEANING')], max_length=12, null=True),
        ),
    ]