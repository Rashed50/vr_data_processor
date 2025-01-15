from django.db import models

# Create your models here.

class VUser(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    
    class Meta:
        db_table ='VUser'
        ordering = ['name']


# class VRModel(models.Model):

#     sessionId    = models.CharField(max_length=150)    
#     frameNumber = models.CharField(max_length=20)    
#     timestamp    = models.CharField(max_length=150)  
#     topic  = models.TextField(max_length=500,default="")   
#     sensorData  = models.TextField(max_length=500)
#     headUserPresence = models.BooleanField(default=False)
#     headIsTracked = models.BooleanField(default=False)
#     headTrackingState = models.SmallIntegerField(default=0)
#     headDevicePosition = models.CharField(max_length=30,default="")
#     headDeviceRotation = models.CharField(max_length=30,default="")
#     headDeviceVelocity = models.CharField(max_length=30,default="")
#     headDeviceAngularVelocity = models.CharField(max_length=30,default="")
#     headCenterEyePosition = models.CharField(max_length=30,default="")
#     headCenterEyeRotation  = models.CharField(max_length=30,default="")
#     headCenterEyeVelocity  = models.CharField(max_length=30,default="")
#     headCenterEyeAngularVelocity  = models.CharField(max_length=30,default="")
#     headLeftEyePosition  = models.CharField(max_length=30,default="")
#     headLeftEyeRotation  = models.CharField(max_length=50,default="")
#     headLeftEyeVelocity  = models.CharField(max_length=30,default="")
#     headLeftEyeAngularVelocity =  models.CharField(max_length=30,default="")
#     headRightEyePosition  = models.CharField(max_length=30,default="")
#     headRightEyeRotation  = models.CharField(max_length=30,default="")
#     headRightEyeVelocity  = models.CharField(max_length=30,default="")
#     headRightEyeAngularVelocity  = models.CharField(max_length=30,default="")
#     ctrlrLeftPrimary2DAxis  = models.CharField(max_length=30,default="")
#     ctrlrLeftGrip =  models.SmallIntegerField(default=0)
#     ctrlrLeftGripButton = models.BooleanField(default=False)
#     ctrlrLeftMenuButton  = models.BooleanField(default=False)
#     ctrlrLeftPrimaryButton  = models.BooleanField(default=False)
#     ctrlrLeftPrimaryTouch  = models.BooleanField(default=False)
#     ctrlrLeftSecondaryButton  = models.BooleanField(default=False)
#     ctrlrLeftSecondaryTouch  = models.BooleanField(default=False)
#     ctrlrLeftTrigger  = models.BooleanField(default=False)
#     ctrlrLeftTriggerButton  = models.BooleanField(default=False)
#     ctrlrLeftTriggerTouch  = models.BooleanField(default=False)
#     ctrlrLeftPrimary2DAxisClick  = models.BooleanField(default=False)
#     ctrlrLeftPrimary2DAxisTouch  = models.BooleanField(default=False)
#     ctrlrLeftThumbrestTouch  = models.BooleanField(default=False)
#     ctrlrLeftDeviceIsTracked  = models.BooleanField(default=False)
#     ctrlrLeftDeviceTrackingState = models.SmallIntegerField(default=0)
#     ctrlrLeftDevicePosition   = models.CharField(max_length=30,default="")
#     ctrlrLeftDeviceRotation  = models.CharField(max_length=50,default="")
#     ctrlrLeftDeviceVelocity  = models.CharField(max_length=30,default="")
#     ctrlrLeftDeviceAngularVelocity  = models.CharField(max_length=30,default="")
#     ctrlrLeftPointerIsTracked  = models.BooleanField(default=False)
#     ctrlrLeftPointerTrackingState = models.SmallIntegerField(default=0)
#     ctrlrLeftPointerPosition  = models.CharField(max_length=30,default="")
#     ctrlrLeftPointerRotation   = models.CharField(max_length=30,default="")
#     ctrlrLeftPointerVelocity  = models.CharField(max_length=30,default="")
#     ctrlrLeftPointerAngularVelocity  = models.CharField(max_length=30,default="")
#     ctrlrLeftIsTracked   = models.BooleanField(default=False)
#     ctrlrLeftTrackingState = models.SmallIntegerField(default=0)
#     ctrlrRightPrimary2DAxis  = models.CharField(max_length=30,default="")
#     ctrlrRightGrip = models.SmallIntegerField(default=0)
#     ctrlrRightGripButton   = models.BooleanField(default=False)
#     ctrlrRightMenuButton  = models.BooleanField(default=False)
#     ctrlrRightPrimaryButton  = models.BooleanField(default=False)
#     ctrlrRightPrimaryTouch  = models.BooleanField(default=False)
#     ctrlrRightSecondaryButton  = models.BooleanField(default=False)
#     ctrlrRightSecondaryTouch  = models.BooleanField(default=False)
#     ctrlrRightTrigger = models.SmallIntegerField(default=0)
#     ctrlrRightTriggerButton  = models.BooleanField(default=False)
#     ctrlrRightTriggerTouch  = models.BooleanField(default=False)
#     ctrlrRightPrimary2DAxisClick  = models.BooleanField(default=False)
#     ctrlrRightPrimary2DAxisTouch  = models.BooleanField(default=False)
#     ctrlrRightThumbrestTouch  = models.BooleanField(default=False)
#     ctrlrRightDeviceIsTracked  = models.BooleanField(default=False)
#     ctrlrRightDeviceTrackingState = models.SmallIntegerField(default=0)
#     ctrlrRightDevicePosition  = models.CharField(max_length=30,default="")
#     ctrlrRightDeviceRotation  = models.CharField(max_length=50,default="")
#     ctrlrRightDeviceVelocity  = models.CharField(max_length=30,default="")
#     ctrlrRightDeviceAngularVelocity  = models.CharField(max_length=30,default="")
#     ctrlrRightPointerIsTracked  = models.BooleanField(default=False)
#     ctrlrRightPointerTrackingState = models.SmallIntegerField(default=0)
#     ctrlrRightPointerPosition  = models.CharField(max_length=30,default="")
#     ctrlrRightPointerRotation  = models.CharField(max_length=30,default="")
#     ctrlrRightPointerVelocity  = models.CharField(max_length=30,default="")
#     ctrlrRightPointerAngularVelocity  = models.CharField(max_length=30,default="")
#     ctrlrRightIsTracked  = models.BooleanField(default=False)
#     ctrlrRightTrackingState = models.SmallIntegerField(default=0)
#     eyeLeftRot  = models.CharField(max_length=50,default="")
#     eyeRightRot  = models.CharField(max_length=50,default="")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.sessionId

#     class Meta:
#         db_table ='vr_models'
#         ordering = ['sessionId']
    

