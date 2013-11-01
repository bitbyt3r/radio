#!/usr/bin/python
import xmlrpclib
import readline

s = xmlrpclib.ServerProxy('http://localhost:8000', allow_none=True)
commands = {"play":s.play, "status":s.status, "pause":s.pause}
while True:
  command = raw_input(">")
  command.strip()
  command = command.split(" ")
  if command[0] in commands:
    if len(command) > 1:
      print commands[command[0]](" ".join(command[1:]))
    else:
      print commands[command[0]]()
