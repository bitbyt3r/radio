#!/usr/bin/python
import socket
import pickle
import threading
import Queue
import sys
import time

defaultPort = 3344
defaultHost = 'localhost'

class Server:
  class Listener(threading.Thread):
    def __init__(self, queue, killEvent, host, port, bufferSize):
      threading.Thread.__init__(self)
      self.queue = queue
      self.killEvent = killEvent
      self.host = host
      self.port = port
      self.bufferSize = bufferSize

    def getData(self):
      try: 
        conn, addr = self.socket.accept()
        f = conn.makefile('rb', self.bufferSize)
        data = pickle.load(f)
        f.close() 
        conn.close()
        return (data, addr)
      except socket.timeout:
        return None

    def validMsg(self, message):
      return True

    def stop(self):
      self.socket.close()
      self.running = False

    def run(self):
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.socket.settimeout(5)
      self.socket.bind((self.host, self.port))
      self.socket.listen(1)
      self.running = True
      while self.running:
        if self.killEvent.isSet():
          self.stop()
        else:
          msg = self.getData()
          if msg:
            if self.validMsg(msg):
              self.queue.put_nowait(msg)
        
  def __init__(self, host=defaultHost, port=defaultPort, bufferSize=4096):
    self.host = host
    self.port = port
    self.bufferSize = bufferSize
    self.killEvent = threading.Event()
    self.msgQueue = Queue.Queue()
    self.messages = []
    self.listener = self.Listener(self.msgQueue, self.killEvent, self.host, self.port, self.bufferSize)
    self.listener.setDaemon(False)
    self.listener.start()
 
  def getMessages(self):
    messages = []
    while(not self.msgQueue.empty()):
      messages.append(self.msgQueue.get_nowait())
    return messages

  def stop(self):
    self.killEvent.set()

class Client:
  def __init__(self, host=defaultHost, port=defaultPort, bufferSize=4096):
    self.host = host
    self.port = port
    self.bufferSize = bufferSize
  
  def sendMessage(self, message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((self.host, self.port))
    f = s.makefile('wb', self.bufferSize)
    pickle.dump(message, f, pickle.HIGHEST_PROTOCOL)
    f.close()
    s.close()

class Message:
  def __init__(self, type="", contents=()):
    self.type = type
    self.contents = contents
