import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(4,GPIO.OUT)

# switch_pusuhed==LED Turn Right

while True:
    if (GPIO.input(4)==0):
        GPIO.output(4,GPIO.HIGH)
        time.sleep(1)
    