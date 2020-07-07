import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

#Turn on Red LED
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)

#Turn on Yellow LED
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
GPIO.output(24,GPIO.LOW)

#Turn on Red LED
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)

#Turn on Yellow LED
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
GPIO.output(24,GPIO.LOW)

#Turn on Red LED
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
GPIO.output(18,GPIO.LOW)

#Turn on Yellow LED
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
GPIO.output(24,GPIO.LOW)
