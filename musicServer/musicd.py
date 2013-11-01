#!/usr/bin/python
import network
import os
import threading
import traceback
import mpylayer
#import songDB

server = network.Server(port=8080)

try:
  mp = mpylayer.MPlayerControl()
  paused = False
  while True:
    msgs = server.getMessages()
    for i in msgs:
      addr = i[1]
      msg = i[0]
      if msg.type == "play":
        song = msg.contents[0]
        if os.path.exists(song):
          mp.loadfile(song)
        if paused:
          paused = False
          mp.pause()
      if msg.type == "status":
        client = network.Client(host=addr[0], port=8081)
        client.sendMessage(network.Message(type="statusResponse", contents=(mp.percent_pos,)))
      if msg.type == "pause":
        mp.pause()
        paused = not(paused)
except:
  server.stop()
  print traceback.format_exc()

