import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
GPIO.setup(10,GPIO.OUT)
while True:
    if GPIO.input(8)==True:
        GPIO.output(10,True)
    else:
        GPIO.output(10,True)
        time.sleep(1)
        GPIO.output(10,False)
        time.sleep(1)
    

    

