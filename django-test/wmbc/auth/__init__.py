#!/usr/bin/python
from models import User
from backends import ModelBackend
import time
import subprocess

class KerberosAuth(ModelBackend):
  def __init__(self):
    self = self

  def authenticate(self, username, password):
    if username and password:
      try:
        authProc = subprocess.Popen('/home/mark25/projects/radio/django-test/wmbc/auth/auth.pl', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        authProc.stdin.write(username+"\n"+password+"\n")
        authReturn = authProc.stdout.read()
      except:
        return None
    else:
      return None
    if authReturn == "Success":
      user = None
      try:
        user = User.objects.get(username=username)
      except User.DoesNotExist:
        user = User(username=username, password='We Dont Store Passwords Here. Sorry, try a worse website to steal them.')
        if username in ['mark25', 'zstewar1']:
          user.is_staff = True
          user.is_superuser = True
        user.save()
      return user
    else:
      return None

  def get_user(self, user_id):
    try:
      return User.objects.get(pk=user_id)
    except User.DoesNotExist:
      return None
