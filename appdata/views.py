from django.shortcuts import render
#from appdata.models import VRModel
# Create your views here.

def datastore(sessionId):
    storeIncomingData()
    print(sessionId)

def storeIncomingData(topic,payload): 
   # payload = json.loads(payload) # extraction json     
    print(f'\n 2.Received message for storing in database ====== topic: {topic} with payload:{payload} ')

    session_id = payload['session_id'] # random.randrange(1111,9999)
    frame_number = payload['frame_number'] # random.randrange(99999,999999)
    timestamp = payload['timestamp'] # time.time()
    msg = payload['msg']

    # sensor_data = {
    # "incoming_message":msg,
    # "HeadUserPresence": False,
    # "HeadIsTracked": False,
    # "HeadTrackingState": 0,
    # "HeadDevicePosition": "(0.00, 0.00, 0.00)"
    # }

#    "msg": "this is testing message from mqttx app oooooo",
#   "session_id" : "546464646",
#   "frame_number" : 6549671763,
#   "timestamp" : 1734351949


   # convert into JSON:
  #  sensor_data = json.dumps(sensor_data)
   # data = VRModel(sessionId= session_id,frameNumber=frame_number,topic=topic,message= msg)
    #data = VRModel.objects.create(sessionId=session_id,frameNumber=frame_number,topic=topic,message=msg) # ORM system 
   # data.save()
    print(f'data store in db ==')

