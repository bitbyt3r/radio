#!/usr/bin/python
import mysqldb

username = "radio"
password = "radioTest"
host = "localhost"
database = "radio"

def startDB():
  db = mysqldb.connect(passwd=password, host=host, user=username, db=database)
  return db

def initializeDB():
  db.execute("""

db = startDB()
