import paho.mqtt.client as mqtt
from hcrcode import hcr
from time import sleep 

# define static variable
# broker = "localhost" # for local connection
broker = "broker.hivemq.com"  # for online version
port = 1883
timeout = 60

username = 'campuspedia'
password = 'qlue'
topic = "teslagrandson/ninno"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
def on_publish(client,userdata,result):
	print("data published \n")
	


client1 = mqtt.Client("hariz")
client1.username_pw_set(username=username,password=password)
client1.on_connect = on_connect
client1.on_publish = on_publish
client1.connect(broker,port,timeout)


while True:
	sensor = hcr()
	message = sensor
	ret = client1.publish(topic,payload=message)