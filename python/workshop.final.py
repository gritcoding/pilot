import time
import picamera
import RPi.GPIO as GPIO  
from subprocess import call
from twilio.rest import TwilioRestClient 

GPIO.setmode(GPIO.BCM)  
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)  
GPIO.setup(21, GPIO.OUT)

ACCOUNT_SID = "AC7b6d99f75b838ce7d2a2c6f429b37fb8" 
AUTH_TOKEN = "57ecc8d16582c939db6cede0c274aa0f" 
 
FROM = "+85264506543"
TO = "61116241"
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

with picamera.PiCamera() as camera:
    camera.start_preview()
    GPIO.wait_for_edge(17, GPIO.FALLING)
    
    for i in range(3):
        time.sleep(0.5)
        GPIO.output(21, 1)
        time.sleep(0.5)
        GPIO.output(21, 0)
 
    call(["aplay", "/usr/share/scratch/Media/Sounds/Animal/Meow.wav"])

    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
    client.messages.create(to=TO, from_=FROM, body="Hello Kitty")
    
GPIO.cleanup()
