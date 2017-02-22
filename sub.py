import paho.mqtt.client as mqtt
import os
import socket
import ssl
import json

#  thing = "dev-cadec-messagesX"
thing = "00000273"
topic = "$aws/things/"+thing+"/shadow/update"

def on_connect(mqttc, obj, flags, rc):
    print("Connection")
    if rc==0:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: successful")
    elif rc==1:
        print ("Subscriber Connection status code: "+str(rc)+" | Connection status: Connection refused")

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos)+"data"+str(obj))
    

def on_message(mqttc, obj, msg):
    print("Received message from topic: "+msg.topic+" | QoS: "+str(msg.qos)+" | Data Received: "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("Message is published")

def first_message():
    payload = json.dumps({
        "state":{
            "reported":{
                "temperature":23.5,
            }
        }
    })
    mqttc.publish(topic, payload)

    
clientId = thing 
mqttc = mqtt.Client(clientId)
# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Connect
#  awshost = "a31ovqfkmg1ev8.iot.eu-west-1.amazonaws.com"
awshost = "a3k7odshaiipe8.iot.eu-west-1.amazonaws.com"
awsport = 8883
caPath = "./things/root.crt"
certPath = "./things/"+thing+"/cert.pem"
keyPath = "./things/"+thing+"/privkey.pem"
print("SSL version: "+ssl.OPENSSL_VERSION)

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)
mqttc.subscribe(topic+"/#", qos=1)
#first_message()

# Continue the network loop
mqttc.loop_forever()


