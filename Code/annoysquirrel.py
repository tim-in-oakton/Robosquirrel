import requests
import io

# take the credential key that you got from your webhook in IFTTT and put it in this file as a single line of text
IFTTT_APPLICATION_FILE = "/home/pi/iftttcreds.txt"

with open (IFTTT_APPLICATION_FILE, "r") as credfile:
    IFTTT_APPLICATION_CREDENTIALS=credfile.readlines()

def annoySquirrelOn():
        requests.get('https://maker.ifttt.com/trigger/squirrelOn/with/key/',IFTTT_APPLICATION_CREDENTIALS)

def annoySquirrelOff():
        requests.get('https://maker.ifttt.com/trigger/squirrelOff/with/key/',IFTTT_APPLICATION_CREDENTIALS)
