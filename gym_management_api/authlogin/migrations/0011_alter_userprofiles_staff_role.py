# Generated by Django 3.2 on 2021-06-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authlogin', '0010_userprofiles_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='staff_role',
            field=models.CharField(choices=[('TRAINER', 'TRAINER'), ('PTRAIN', 'PTRAIN'), ('ACCOUNTANT', 'ACCOUNTANT'), ('CLEANING', 'CLEANING')], max_length=12, null=True),
        ),
    ]
