import json
import requests
import base64
import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# UPDATE:
url = "https://api.github.com/repos/<your username>/<your repo>/contents/syntheticHealth.txt"

#Get certain file content
print("Application running... to stop type control-C")
while True:
    r = requests.get(url).text
    a = json.loads(r)

    if str(base64.b64decode(a["content"]))[2] == "2":
        GPIO.output(18,GPIO.HIGH)
        GPIO.output(24,GPIO.LOW)
        print("Critical error")
    elif str(base64.b64decode(a["content"]))[2] == "1":
        GPIO.output(24,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        print("Warning")
    elif str(base64.b64decode(a["content"]))[2] == "0":
        GPIO.output(24,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
    time.sleep(10)
