import RPi.GPIO as GPIO

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)#output pin is GPIO-4

GPIO.output(4,GPIO.HIGH)
