import paho.mqtt.client as mqtt
import sys


input = sys.argv[1]

broker="104.238.164.118"
port=8883

client1 = mqtt.Client("ClientName") # Doesnt matter
client1.connect(broker,port)
ret=client1.publish("tagger/rpi/bt",input)

