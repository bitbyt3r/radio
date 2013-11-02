#!/usr/bin/python
import subprocess

def authenticate(username, password):
  if username and password:
    try:
      authProc = subprocess.Popen('./auth.pl', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
      authProc.stdin.write(username+"\n"+password+"\n")
      authReturn = authProc.stdout.read()
    except:
      return False
  else:
    return False
  if authReturn == "Success":
    return True
  else:
    return False
