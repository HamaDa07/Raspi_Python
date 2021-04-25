import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

count=0

while True:
    if(GPIO.input(4)==0):
        count=count+1
        #switch_puscd+=1
        
        print("Count;"+str(count))
        
        #if switch leaved
        while(GPIO.input(4)==0):
            time.sleep(0.1)
            # add delay ... raspi = raight
            
              