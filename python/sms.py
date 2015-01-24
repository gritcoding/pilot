from twilio.rest import TwilioRestClient 

ACCOUNT_SID = "AC7b6d99f75b838ce7d2a2c6f429b37fb8" 
AUTH_TOKEN = "57ecc8d16582c939db6cede0c274aa0f" 
 
FROM = "+85264506543"
TO = "95417352"
NAME = "Alice"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
client.messages.create(to=TO, from_=FROM,
                       body="Hello " + NAME)

print("Sent sms to " + NAME)
