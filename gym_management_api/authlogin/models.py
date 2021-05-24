from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class MasterGyms(models.Model):

    gym_name = models.TextField(null=False)
    owner_first_name = models.CharField(max_length=50, null=False)
    owner_last_name = models.CharField(max_length=50, null=False)
    active_subscription = models.BooleanField(default=True, null=False)
    last_login_ip = models.GenericIPAddressField()
    country_code = models.IntegerField(null=False)
    contact_number = models.TextField(null=False)
    owner_email = models.EmailField(null=False)


class OwnerPassReset(models.Model):

    gym_name = models.TextField()
    gym_email = models.EmailField()
    ip_address = models.GenericIPAddressField()
    token_id = models.TextField()
    is_active = models.BooleanField(default=True)
    attempted_at = models.DateTimeField(auto_now_add=True)


class GymData(models.Model):

    gym_name = models.TextField(null=False)
    gym_address = models.TextField(null=False)
    gym_country = models.TextField(null=False)

    def __str__(self):
        return self.gym_name


class UserProfiles(models.Model):

    username = models.TextField(null=False)
    password = models.TextField(null=False)
    email = models.TextField(null=False)
    phone_number = models.TextField(null=False)
    country_code = models.IntegerField(null=False)
    location = models.TextField(null=False)
    is_owner = models.BooleanField(default=False)
    gym_id = models.ForeignKey(GymData, models.CASCADE, null=True)
    last_login_ip = models.GenericIPAddressField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
