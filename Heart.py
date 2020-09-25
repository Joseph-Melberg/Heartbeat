import os
import time
import subprocess
import pika
import json
import time
def system_call(command):
    p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
    return p.stdout.read()

credentials = pika.PlainCredentials('life','conway')
connection = pika.BlockingConnection(pika.ConnectionParameters('centurionx.net',5672,'/',credentials))
channel = connection.channel()
messa = {}
messa["Name"] = "skywatcher"
def getMAC(interface='eth0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

messa["Mac"] = getMAC()

channel.basic_publish(exchange='Inter',
                      routing_key='/life',
                      body=str(messa))
connection.close()
