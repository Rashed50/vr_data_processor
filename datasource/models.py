from django.db import models
import time,json
# Create your models here.
from dataclasses import dataclass
 


class VRModel(models.Model):

    sessionId    = models.CharField(max_length=150)    
    frameNumber = models.CharField(max_length=20)    
    timestamp    = models.CharField(max_length=150)  
    topic  = models.TextField(max_length=500,default="")   
    sensorData  = models.TextField(max_length=500)
    headUserPresence = models.BooleanField(default=False)
    headIsTracked = models.BooleanField(default=False)
    headTrackingState = models.SmallIntegerField(default=0)
    headDevicePosition = models.CharField(max_length=30,default="")
    headDeviceRotation = models.CharField(max_length=30,default="")
    headDeviceVelocity = models.CharField(max_length=30,default="")
    headDeviceAngularVelocity = models.CharField(max_length=30,default="")
    headCenterEyePosition = models.CharField(max_length=30,default="")
    headCenterEyeRotation  = models.CharField(max_length=30,default="")
    headCenterEyeVelocity  = models.CharField(max_length=30,default="")
    headCenterEyeAngularVelocity  = models.CharField(max_length=30,default="")
    headLeftEyePosition  = models.CharField(max_length=30,default="")
    headLeftEyeRotation  = models.CharField(max_length=50,default="")
    headLeftEyeVelocity  = models.CharField(max_length=30,default="")
    headLeftEyeAngularVelocity =  models.CharField(max_length=30,default="")
    headRightEyePosition  = models.CharField(max_length=30,default="")
    headRightEyeRotation  = models.CharField(max_length=30,default="")
    headRightEyeVelocity  = models.CharField(max_length=30,default="")
    headRightEyeAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftPrimary2DAxis  = models.CharField(max_length=30,default="")
    ctrlrLeftGrip =  models.SmallIntegerField(default=0)
    ctrlrLeftGripButton = models.BooleanField(default=False)
    ctrlrLeftMenuButton  = models.BooleanField(default=False)
    ctrlrLeftPrimaryButton  = models.BooleanField(default=False)
    ctrlrLeftPrimaryTouch  = models.BooleanField(default=False)
    ctrlrLeftSecondaryButton  = models.BooleanField(default=False)
    ctrlrLeftSecondaryTouch  = models.BooleanField(default=False)
    ctrlrLeftTrigger  = models.BooleanField(default=False)
    ctrlrLeftTriggerButton  = models.BooleanField(default=False)
    ctrlrLeftTriggerTouch  = models.BooleanField(default=False)
    ctrlrLeftPrimary2DAxisClick  = models.BooleanField(default=False)
    ctrlrLeftPrimary2DAxisTouch  = models.BooleanField(default=False)
    ctrlrLeftThumbrestTouch  = models.BooleanField(default=False)
    ctrlrLeftDeviceIsTracked  = models.BooleanField(default=False)
    ctrlrLeftDeviceTrackingState = models.SmallIntegerField(default=0)
    ctrlrLeftDevicePosition   = models.CharField(max_length=30,default="")
    ctrlrLeftDeviceRotation  = models.CharField(max_length=50,default="")
    ctrlrLeftDeviceVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftDeviceAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftPointerIsTracked  = models.BooleanField(default=False)
    ctrlrLeftPointerTrackingState = models.SmallIntegerField(default=0)
    ctrlrLeftPointerPosition  = models.CharField(max_length=30,default="")
    ctrlrLeftPointerRotation   = models.CharField(max_length=30,default="")
    ctrlrLeftPointerVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftPointerAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftIsTracked   = models.BooleanField(default=False)
    ctrlrLeftTrackingState = models.SmallIntegerField(default=0)
    ctrlrRightPrimary2DAxis  = models.CharField(max_length=30,default="")
    ctrlrRightGrip = models.SmallIntegerField(default=0)
    ctrlrRightGripButton   = models.BooleanField(default=False)
    ctrlrRightMenuButton  = models.BooleanField(default=False)
    ctrlrRightPrimaryButton  = models.BooleanField(default=False)
    ctrlrRightPrimaryTouch  = models.BooleanField(default=False)
    ctrlrRightSecondaryButton  = models.BooleanField(default=False)
    ctrlrRightSecondaryTouch  = models.BooleanField(default=False)
    ctrlrRightTrigger = models.SmallIntegerField(default=0)
    ctrlrRightTriggerButton  = models.BooleanField(default=False)
    ctrlrRightTriggerTouch  = models.BooleanField(default=False)
    ctrlrRightPrimary2DAxisClick  = models.BooleanField(default=False)
    ctrlrRightPrimary2DAxisTouch  = models.BooleanField(default=False)
    ctrlrRightThumbrestTouch  = models.BooleanField(default=False)
    ctrlrRightDeviceIsTracked  = models.BooleanField(default=False)
    ctrlrRightDeviceTrackingState = models.SmallIntegerField(default=0)
    ctrlrRightDevicePosition  = models.CharField(max_length=30,default="")
    ctrlrRightDeviceRotation  = models.CharField(max_length=50,default="")
    ctrlrRightDeviceVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightDeviceAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightPointerIsTracked  = models.BooleanField(default=False)
    ctrlrRightPointerTrackingState = models.SmallIntegerField(default=0)
    ctrlrRightPointerPosition  = models.CharField(max_length=30,default="")
    ctrlrRightPointerRotation  = models.CharField(max_length=30,default="")
    ctrlrRightPointerVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightPointerAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightIsTracked  = models.BooleanField(default=False)
    ctrlrRightTrackingState = models.SmallIntegerField(default=0)
    eyeLeftRot  = models.CharField(max_length=50,default="")
    eyeRightRot  = models.CharField(max_length=50,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sessionId

    class Meta:
        db_table ='vr_models'
        ordering = ['sessionId']


        
# class TimestampedModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
#         ordering = ['-created_at', '-updated_at']




# class VRModel():


    # def __init__(self, sessionId,frameNumber,topic,message):
    #     super().__init__()
    #     self.sessionID    = sessionId
    #     self.frameNumber = frameNumber
    #     self.timestamp    = time.time()
    #     self.topic  = topic
    #     self.sensorData  = message
    #     self.headUserPresence = False
    #     self.headIsTracked = False
    #     self.headTrackingState = 0
    #     self.headDevicePosition =  ""
    #     self.headDeviceRotation = ""
    #     self.headDeviceVelocity = ""
    #     self.headDeviceAngularVelocity =  ""
    #     self.headCenterEyePosition = ""
    #     self.headCenterEyeRotation  =  ""
    #     self.headCenterEyeVelocity  = ""
    #     self.headCenterEyeAngularVelocity  = ""
    #     self.headLeftEyePosition  = ""
    #     self.headLeftEyeRotation  = ""
    #     self.headLeftEyeVelocity  = ""
    #     self.headLeftEyeAngularVelocity = ""
    #     self.headRightEyePosition  = ""
    #     self.headRightEyeRotation  = ""
    #     self.headRightEyeVelocity  = ""
    #     self.headRightEyeAngularVelocity  = ""
    #     self.ctrlrLeftPrimary2DAxis  = ""
    #     self.ctrlrLeftGrip =  0
    #     self.ctrlrLeftGripButton = False
    #     self.ctrlrLeftMenuButton  = False
    #     self.ctrlrLeftPrimaryButton  = False
    #     self.ctrlrLeftPrimaryTouch  = False
    #     self.ctrlrLeftSecondaryButton  = False
    #     self.ctrlrLeftSecondaryTouch  = False
    #     self.ctrlrLeftTrigger  = False
    #     self.ctrlrLeftTriggerButton  = False
    #     self.ctrlrLeftTriggerTouch  = False
    #     self.ctrlrLeftPrimary2DAxisClick  = False
    #     self.ctrlrLeftPrimary2DAxisTouch  = False
    #     self.ctrlrLeftThumbrestTouch  = False
    #     self.ctrlrLeftDeviceIsTracked  = False
    #     self.ctrlrLeftDeviceTrackingState = 0
    #     self.ctrlrLeftDevicePosition   = ""
    #     self.ctrlrLeftDeviceRotation  = ""
    #     self.ctrlrLeftDeviceVelocity  = ""
    #     self.ctrlrLeftDeviceAngularVelocity  = ""
    #     self.ctrlrLeftPointerIsTracked  = False
    #     self.ctrlrLeftPointerTrackingState = 0
    #     self.ctrlrLeftPointerPosition  = ""
    #     self.ctrlrLeftPointerRotation   = ""
    #     self.ctrlrLeftPointerVelocity  = ""
    #     self.ctrlrLeftPointerAngularVelocity  = ""
    #     self.ctrlrLeftIsTracked   = False
    #     self.ctrlrLeftTrackingState = 0
    #     self.ctrlrRightPrimary2DAxis =""
    #     self.ctrlrRightGrip = 0
    #     self.ctrlrRightGripButton   = False
    #     self.ctrlrRightMenuButton  = False
    #     self.ctrlrRightPrimaryButton  = False
    #     self.ctrlrRightPrimaryTouch  = False
    #     self.ctrlrRightSecondaryButton  = False
    #     self.ctrlrRightSecondaryTouch  = False
    #     self.ctrlrRightTrigger = 0
    #     self.ctrlrRightTriggerButton  = False
    #     self.ctrlrRightTriggerTouch  = False
    #     self.ctrlrRightPrimary2DAxisClick  = False
    #     self.ctrlrRightPrimary2DAxisTouch  = False
    #     self.ctrlrRightThumbrestTouch  = False
    #     self.ctrlrRightDeviceIsTracked  = False
    #     self.ctrlrRightDeviceTrackingState = 0
    #     self.ctrlrRightDevicePosition  = ""
    #     self.ctrlrRightDeviceRotation  = ""
    #     self.ctrlrRightDeviceVelocity  = ""
    #     self.ctrlrRightDeviceAngularVelocity  = ""
    #     self.ctrlrRightPointerIsTracked  = False
    #     self.ctrlrRightPointerTrackingState = 0
    #     self.ctrlrRightPointerPosition  = ""
    #     self.ctrlrRightPointerRotation  = ""
    #     self.ctrlrRightPointerVelocity  = ""
    #     self.ctrlrRightPointerAngularVelocity  = ""
    #     self.ctrlrRightIsTracked  = False
    #     self.ctrlrRightTrackingState = 0
    #     self.eyeLeftRot  = ""
    #     self.eyeRightRot  = ""

   
    #sessionID    = models.CharField(max_length=150)    
    # frameNumber = models.CharField(max_length=20)    
    # timestamp    = models.CharField(max_length=150)  
    # topic  = models.TextField(max_length=500,default="")   
    # sensorData  = models.TextField(max_length=500)
    # headUserPresence = models.BooleanField(default=False)
    # headIsTracked = models.BooleanField(default=False)
    # headTrackingState = models.SmallIntegerField(default=0)
    # headDevicePosition = models.CharField(max_length=30,default="")
    # headDeviceRotation = models.CharField(max_length=30,default="")
    # headDeviceVelocity = models.CharField(max_length=30,default="")
    # headDeviceAngularVelocity = models.CharField(max_length=30,default="")
    # headCenterEyePosition = models.CharField(max_length=30,default="")
    # headCenterEyeRotation  = models.CharField(max_length=30,default="")
    # headCenterEyeVelocity  = models.CharField(max_length=30,default="")
    # headCenterEyeAngularVelocity  = models.CharField(max_length=30,default="")
    # headLeftEyePosition  = models.CharField(max_length=30,default="")
    # headLeftEyeRotation  = models.CharField(max_length=50,default="")
    # headLeftEyeVelocity  = models.CharField(max_length=30,default="")
    # headLeftEyeAngularVelocity =  models.CharField(max_length=30,default="")
    # headRightEyePosition  = models.CharField(max_length=30,default="")
    # headRightEyeRotation  = models.CharField(max_length=30,default="")
    # headRightEyeVelocity  = models.CharField(max_length=30,default="")
    # headRightEyeAngularVelocity  = models.CharField(max_length=30,default="")
    # ctrlrLeftPrimary2DAxis  = models.CharField(max_length=30,default="")
    # ctrlrLeftGrip =  models.SmallIntegerField(default=0)
    # ctrlrLeftGripButton = models.BooleanField(default=False)
    # ctrlrLeftMenuButton  = models.BooleanField(default=False)
    # ctrlrLeftPrimaryButton  = models.BooleanField(default=False)
    # ctrlrLeftPrimaryTouch  = models.BooleanField(default=False)
    # ctrlrLeftSecondaryButton  = models.BooleanField(default=False)
    # ctrlrLeftSecondaryTouch  = models.BooleanField(default=False)
    # ctrlrLeftTrigger  = models.BooleanField(default=False)
    # ctrlrLeftTriggerButton  = models.BooleanField(default=False)
    # ctrlrLeftTriggerTouch  = models.BooleanField(default=False)
    # ctrlrLeftPrimary2DAxisClick  = models.BooleanField(default=False)
    # ctrlrLeftPrimary2DAxisTouch  = models.BooleanField(default=False)
    # ctrlrLeftThumbrestTouch  = models.BooleanField(default=False)
    # ctrlrLeftDeviceIsTracked  = models.BooleanField(default=False)
    # ctrlrLeftDeviceTrackingState = models.SmallIntegerField(default=0)
    # ctrlrLeftDevicePosition   = models.CharField(max_length=30,default="")
    # ctrlrLeftDeviceRotation  = models.CharField(max_length=50,default="")
    # ctrlrLeftDeviceVelocity  = models.CharField(max_length=30,default="")
    # ctrlrLeftDeviceAngularVelocity  = models.CharField(max_length=30,default="")
    # ctrlrLeftPointerIsTracked  = models.BooleanField(default=False)
    # ctrlrLeftPointerTrackingState = models.SmallIntegerField(default=0)
    # ctrlrLeftPointerPosition  = models.CharField(max_length=30,default="")
    # ctrlrLeftPointerRotation   = models.CharField(max_length=30,default="")
    # ctrlrLeftPointerVelocity  = models.CharField(max_length=30,default="")
    # ctrlrLeftPointerAngularVelocity  = models.CharField(max_length=30,default="")
    # ctrlrLeftIsTracked   = models.BooleanField(default=False)
    # ctrlrLeftTrackingState = models.SmallIntegerField(default=0)
    # ctrlrRightPrimary2DAxis  = models.CharField(max_length=30,default="")
    # ctrlrRightGrip = models.SmallIntegerField(default=0)
    # ctrlrRightGripButton   = models.BooleanField(default=False)
    # ctrlrRightMenuButton  = models.BooleanField(default=False)
    # ctrlrRightPrimaryButton  = models.BooleanField(default=False)
    # ctrlrRightPrimaryTouch  = models.BooleanField(default=False)
    # ctrlrRightSecondaryButton  = models.BooleanField(default=False)
    # ctrlrRightSecondaryTouch  = models.BooleanField(default=False)
    # ctrlrRightTrigger = models.SmallIntegerField(default=0)
    # ctrlrRightTriggerButton  = models.BooleanField(default=False)
    # ctrlrRightTriggerTouch  = models.BooleanField(default=False)
    # ctrlrRightPrimary2DAxisClick  = models.BooleanField(default=False)
    # ctrlrRightPrimary2DAxisTouch  = models.BooleanField(default=False)
    # ctrlrRightThumbrestTouch  = models.BooleanField(default=False)
    # ctrlrRightDeviceIsTracked  = models.BooleanField(default=False)
    # ctrlrRightDeviceTrackingState = models.SmallIntegerField(default=0)
    # ctrlrRightDevicePosition  = models.CharField(max_length=30,default="")
    # ctrlrRightDeviceRotation  = models.CharField(max_length=50,default="")
    # ctrlrRightDeviceVelocity  = models.CharField(max_length=30,default="")
    # ctrlrRightDeviceAngularVelocity  = models.CharField(max_length=30,default="")
    # ctrlrRightPointerIsTracked  = models.BooleanField(default=False)
    # ctrlrRightPointerTrackingState = models.SmallIntegerField(default=0)
    # ctrlrRightPointerPosition  = models.CharField(max_length=30,default="")
    # ctrlrRightPointerRotation  = models.CharField(max_length=30,default="")
    # ctrlrRightPointerVelocity  = models.CharField(max_length=30,default="")
    # ctrlrRightPointerAngularVelocity  = models.CharField(max_length=30,default="")
    # ctrlrRightIsTracked  = models.BooleanField(default=False)
    # ctrlrRightTrackingState = models.SmallIntegerField(default=0)
    # eyeLeftRot  = models.CharField(max_length=50,default="")
    # eyeRightRot  = models.CharField(max_length=50,default="")
    #created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     db_table ='vr_models'
    #     ordering = ['sessionID']




