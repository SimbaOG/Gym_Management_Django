from django.apps import AppConfig

MAIN_DIR = 'gym_management_api'


class AuthloginConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'{MAIN_DIR}.authlogin'
