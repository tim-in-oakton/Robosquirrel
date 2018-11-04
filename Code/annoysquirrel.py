import requests
import io
import time

# take the credential key that you got from your webhook in IFTTT and put it in this file as a single line of text
IFTTT_APPLICATION_FILE = "/home/pi/iftttcreds.txt"

with open (IFTTT_APPLICATION_FILE, "r") as credfile:
    IFTTT_APPLICATION_CREDENTIALS=credfile.read()

def annoySquirrelOn():
    sendstring='https://maker.ifttt.com/trigger/squirrelOn/with/key/'+IFTTT_APPLICATION_CREDENTIALS
    print(sendstring)
    r=requests.get('https://maker.ifttt.com/trigger/squirrelOn/with/key/'+IFTTT_APPLICATION_CREDENTIALS)
    print(r)
    time.sleep(2)

def annoySquirrelOff():
    sendstring='https://maker.ifttt.com/trigger/squirrelOff/with/key/'+IFTTT_APPLICATION_CREDENTIALS
    print(sendstring)
    r=requests.get('https://maker.ifttt.com/trigger/squirrelOff/with/key/'+IFTTT_APPLICATION_CREDENTIALS)
