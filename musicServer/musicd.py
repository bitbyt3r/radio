#!/usr/bin/python
import network
import os
import threading
import traceback
import mpylayer
#import songDB

server = network.Server(port=4449)
client = network.Client(port=4448)

try:
  mp = mpylayer.MPlayerControl()
  while True:
    msgs = server.getMessages()
    for i in msgs:
      if i.type == "play":
        song = i.contents[0]
        print song
        mp.loadfile(song)
      if i.type == "status":
        client.sendMessage(network.Message(type="statusResponse", contents=(mp.percent_pos,)))
      if i.type == "pause":
        mp.pause()
except:
  server.stop()
  print traceback.format_exc()

