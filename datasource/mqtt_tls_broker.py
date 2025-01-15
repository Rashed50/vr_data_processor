
import paho.mqtt.client as mqtt
import ssl, time, inspect, os
#from appdata.models import VRModel
#from datasource.views import storeIncomingData
from datasource.models import VRModel
import json


broker_address="mgbckr.net" # this must match the CNAME in your server-cert!
topic="vrsensors"

def on_message(client, userdata, message):
    #storeIncomingData(message.topic,message.payload)
    #datastore(1233)
    topic = message.topic
    payload = message.payload
    print(f'\n 1.Received message on_message() {topic}====== {payload},')
    storeIncomingData2(topic,payload)
    
    


def storeIncomingData2(topic,payload): 
    payload = json.loads(payload) # extraction json     
    print(f'\n 2.Received message for storing in database ====== topic: {topic} with payload:{payload} ')

    session_id = payload['session_id'] # random.randrange(1111,9999)
    frame_number =  payload['frame_number'] # random.randrange(99999,999999)
    timestamp =  payload['timestamp'] # time.time()
    msg =   payload['msg']

#     sensor_data = {
#     "incoming_message":msg,
#     "HeadUserPresence": False,
#     "HeadIsTracked": False,
#     "HeadTrackingState": 0,
#     "HeadDevicePosition": "(0.00, 0.00, 0.00)"
#     }

#    "msg": "this is testing message from mqttx app oooooo",
#   "session_id" : "546464646",
#   "frame_number" : 6549671763,
#   "timestamp" : 1734351949


    # convert into JSON:
    #sensor_data = json.dumps(sensor_data)
    #data = VRModel(sessionId= session_id,frameNumber=frame_number,topic=topic,message= msg)
    data = VRModel.objects.create(sessionId=session_id,frameNumber=frame_number,timestamp=timestamp,topic=topic,sensorData=msg) # ORM system 


def startMQTTBroker():
    MQTT_USER = 'vrsensors'
    MQTT_PASSWORD = '*vr!sensors2024'
    print( "creating new instance" )
    client = mqtt.Client()

    print( "connecting to broker")
    client.tls_set("E:\\Germany File\\Martin Becker\\projects\\vr_data_processor\\vr_data_processor\\datasource\\certificate\\client_cert.cer" , tls_version=ssl.PROTOCOL_TLSv1_2)
    # #client.tls_set("datasource\\certificate\\client_cert.cer" , tls_version=ssl.PROTOCOL_TLSv1_2)


    client.tls_insecure_set(False)
    client.username_pw_set(MQTT_USER,MQTT_PASSWORD)
    # # client.tls_set(certfile=None,
    # #                keyfile=None,
    # #                cert_reqs=ssl.CERT_REQUIRED)
    client.connect( broker_address, 8883, 60 )

    client.loop_start()

    print( "Subscribing to topic", topic )
    client.on_message=on_message
    client.subscribe( topic )

    # for i in range( 1, 10 ):
    #     print( "Publishing message to topic" , topic )
    #     client.publish( topic, "Hello, I am from VR-Sensor Data Processor "+str(i) )
    #     time.sleep( 1 )
    # client.loop_stop()

    print( "Goodbye Goodbye!" )