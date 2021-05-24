from hashlib import pbkdf2_hmac
import os


def store_hash_pass(pwd):

    salt = os.urandom(32)
    key = pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt, 100000, dklen=128)
    h_data = salt + key
    return h_data


def decode_pass(hashed_pass):

    h_pass = eval(hashed_pass)

    b_salt = h_pass[:32]
    b_key = h_pass[32:]

    return b_salt, b_key


def compare_passwords(salt, key, pwd):

    crr_key = pbkdf2_hmac('sha256', pwd.encode('utf-8'), salt, 100000, dklen=128)

    if crr_key == key:
        return True
    if crr_key is not key:
        return False
