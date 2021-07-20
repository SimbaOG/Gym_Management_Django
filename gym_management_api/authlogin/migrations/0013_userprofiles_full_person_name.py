# Generated by Django 3.2 on 2021-06-06 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authlogin', '0012_remove_userprofiles_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='full_person_name',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
