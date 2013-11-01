#!/usr/bin/python
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import mpylayer
import os

mp = mpylayer.MPlayerControl()
state = {"transport":"stopped",
         "song":""}

class RequestHandler(SimpleXMLRPCRequestHandler):
  rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

def play(song=None):
  print song
  if os.path.exists(song):
    mp.loadfile(song)
    print "starting"
    state["song"] = song
    if state["transport"] == "paused":
      mp.pause()
      print "unpausing to play"
    state["transport"] = "playing"
    return True
  return False

def status():
  print "getting status"
  return state, mp.percent_pos

def pause():
  if state["transport"] != "paused":
    print "unpausing"
    state["transport"] = "paused"
    mp.pause()
  return True

server.register_function(play)
server.register_function(status)
server.register_function(pause)

server.serve_forever()
