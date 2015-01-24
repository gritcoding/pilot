import RPi.GPIO as GPIO
import picamera
from twilio.rest import TwilioRestClient 

ACCOUNT_SID = "AC7b6d99f75b838ce7d2a2c6f429b37fb8" 
AUTH_TOKEN = "57ecc8d16582c939db6cede0c274aa0f" 
 
FROM = "+85264506543"
TO = "87654321"
DOORBELL = "192.168.1.101"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(17, GPIO.FALLING)
    print("Take picture")
    with picamera.PiCamera() as camera:
        camera.capture('static/image.jpg')
    print("Send SMS to " + TO)
    client.messages.create(to=TO, from_=FROM,
            body="Door Bell! http://" + DOORBELL)
    GPIO.remove_event_detect(17)

