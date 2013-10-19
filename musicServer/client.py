#!/usr/bin/python
import network
import sys
import traceback
import threading

server = network.Server(port=4448)
client = network.Client(port=4449)

class Printer(threading.Thread):
  def __init__(self, server):
    threading.Thread.__init__(self)
    self.server = server
    self.running = True
  def run(self):
    while self.running:
      for i in self.server.getMessages():
        if i.type == "statusResponse":
          sys.stdout.write("\r%s%%\n>" % i.contents[0])
        sys.stdout.flush()
  def stop(self):
    self.running = False

try:
  printer = Printer(server)
  printer.start()
  while True:
    msg = None
    str = raw_input(">")
    str.strip()
    pieces = str.split(" ")
    if pieces[0] == "play":
      msg = network.Message(type="play", contents=(" ".join(pieces[1:]),))
    if pieces[0] == "status":
      msg = network.Message(type="status", contents=())
    if pieces[0] == "pause":
      msg = network.Message(type="pause", contents=())
    if pieces[0] == "exit":
      server.stop()
      printer.stop()
      sys.exit(0)
    if msg:
      client.sendMessage(msg)
except:
  server.stop()
  printer.stop()
#  print traceback.format_exc()
