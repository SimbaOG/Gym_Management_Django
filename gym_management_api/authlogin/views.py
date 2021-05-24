from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
import socket
from uuid import uuid4
from gym_management_api import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from hashlib import pbkdf2_hmac
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
import background_task
import time
import datetime as dt
import os
from .hasher import *
from django.contrib import messages

# Create your views here.

sched = BackgroundScheduler()
sched.start()


def main_page(request):
    log_stat = request.COOKIES.get('UserLogged')
    log_name = request.COOKIES.get('UID')

    if log_stat is None or log_name is None:
        return render(request, 'master_login.html')
    else:
        return render(request, 'dashboard.html')


def load_pass_reset(request):
    return render(request, 'pass_reset.html')


def validate_reset_info(request):
    if request.method == 'POST':
        email = request.POST.get('email', False)

        print("MAIL SEARCHING")

        if MasterGyms.objects.filter(owner_email=email).exists():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                user_ip = x_forwarded_for.split(',')[0]
            else:
                user_ip = request.META.get('REMOTE_ADDR')
            # Getting requester's IP address
            try:
                socket.inet_aton(user_ip)
                ip_valid = True
            except socket.error:
                ip_valid = False

            if ip_valid:
                if OwnerPassReset.objects.filter(gym_email=email, is_active=True).exists:
                    OwnerPassReset.objects.filter(gym_email=email, is_active=True).update(is_active=False)
                    user_token = uuid4()
                    user_token = str(user_token)
                    get_gym_data = MasterGyms.objects.filter(owner_email=email)
                    u_gym_name = get_gym_data[0].gym_name
                    OwnerPassReset.objects.create(gym_email=email, token_id=user_token, is_active=True,
                                                  ip_address=user_ip, gym_name=u_gym_name)

                    own_f_name = get_gym_data[0].owner_first_name
                    subject = f"[no-reply] Password Reset Request for {u_gym_name}"
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    message = "."
                    msg_html = render_to_string('pass_reset_mail.html', {'user': own_f_name,
                                                                         'token_id': user_token,
                                                                         'user_ip': user_ip})

                    send_mail(subject, message, email_from, recipient_list, html_message=msg_html)

                    crr_dt = dt.datetime.now()
                    s_dt = crr_dt + dt.timedelta(minutes=10)

                    sched.add_job(deactivate_token, 'date', run_date=s_dt, args=[user_token])

                    return HttpResponse('')
            else:
                return HttpResponseBadRequest('')
        else:
            return HttpResponseBadRequest('')


def auth_reset_pass(request):
    if request.method == 'GET':
        token_id = request.GET['tkn']
        username = request.GET['us']

        if OwnerPassReset.objects.filter(token_id=token_id, is_active=True).exists():
            return render(request, 'change_pass.html', {'owner_name': username})
        else:
            return render(request, 'failed_pass.html')


def deactivate_token(tokenid):

    OwnerPassReset.objects.filter(token_id=tokenid).update(is_active=False)
    print("Token deactivated")


def auth_master(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Not Valid!")
    else:
        gym_names = GymData.objects.raw('''SELECT * FROM authlogin_gymdata''')
        # print(gym_names[0].gym_name)
        return render(request, 'add_gym_owner.html', {'gymname': gym_names})


def register_owner(request):

    if request.method == 'POST':

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        ph_number = request.POST.get('ph_number', None)
        c_code = request.POST.get('c_code', None)
        loc = request.POST.get('loc', None)
        gym_id = request.POST.get('gym_id', None)

        inp_list = [username, password, email, ph_number, c_code, loc, gym_id]

        gym_obj = GymData.objects.get(id=gym_id)

        if None not in inp_list or "" in inp_list:

            hash_pass = store_hash_pass(password)
            if UserProfiles.objects.filter(username=username).exists():
                return HttpResponseBadRequest('')
            elif UserProfiles.objects.filter(email=email).exists():
                return HttpResponseBadRequest('')
            else:
                UserProfiles.objects.create(username=username, password=hash_pass, email=email, phone_number=ph_number,
                                            country_code=c_code, location=loc, gym_id=gym_obj, is_owner=True)

                return HttpResponse('')

        else:
            return HttpResponseBadRequest('')


def auth_login_user(request):

    if request.method == 'POST':

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if UserProfiles.objects.filter(username=username).exists():
            get_user_profile = UserProfiles.objects.get(username=username)
            user_saved_password = get_user_profile.password

            u_salt, u_key = decode_pass(user_saved_password)

            if compare_passwords(u_salt, u_key, password):
                print("User Logged-In!")
                response = render(request, 'dashboard.html')
                response.set_cookie('UserLogged', True, max_age=settings.SESSION_COOKIE_AGE)
                response.set_cookie('UID', get_user_profile.id, max_age=settings.SESSION_COOKIE_AGE)
                return response
            else:
                print("Credentials Error!")
                messages.error(request, 'username or password incorrect')
                return redirect('/')

        elif UserProfiles.objects.filter(email=username).exists():
            get_user_profile = UserProfiles.objects.get(email=username)
            user_saved_password = get_user_profile.password

            u_salt, u_key = decode_pass(user_saved_password)

            if compare_passwords(u_salt, u_key, password):
                print("User Logged-In!")
                response = render(request, 'dashboard.html')
                response.set_cookie('UserLogged', True, max_age=settings.SESSION_COOKIE_AGE)
                response.set_cookie('UID', get_user_profile.id, max_age=settings.SESSION_COOKIE_AGE)
                return response
            else:
                print("Credentials Error!")
                messages.error(request, 'Username or Password incorrect')
                return redirect('/')

        else:
            messages.error(request, 'Username or Password incorrect')
            return redirect('/')