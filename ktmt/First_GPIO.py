import RPi.GPIO as GPIO
import time
def main():
    #define gia tri cac nut bam
    BT1 = 14
    BT2 = 4
    BT3 = 3
    BT4 = 2
    LED = 22
    GPIO.setmode(GPIO.BCM) #setup mode
    #cai dat cac nut bam la input, pull_up cac nut bam
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #dat den led gia output
    GPIO.setup(LED, GPIO.OUT)
    #dat den led gia tri HIGH
    GPIO.output(LED, GPIO.HIGH)
    ispressBT4 = False
    ispressBT3 = False
    while True:
        if GPIO.input(BT1) == GPIO.LOW: #bam nut 1
            print("BT1 press")
            ispressBT3 = False
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(BT2) == GPIO.LOW: #bam nut 2
            print("BT2 press")
            ispressBT3 = False
            GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.5)
        if GPIO.input(BT3) == GPIO.LOW: #bam nut 3
            print("BT3 press")
            ispressBT3 = True
            GPIO.output(LED, GPIO.LOW)
            time.sleep(0.5)
        if GPIO.input(BT4) == GPIO.LOW: #bam nut 4
            print("BT4 press")
            ispressBT3 = False
            # bam 1 lan den sang, bam 2 lan den tat
            if ispressBT4:
                GPIO.output(LED, GPIO.HIGH)
                ispressBT4 = False
                time.sleep(0.5)
                continue
            if not ispressBT4:
                    GPIO.output(LED, GPIO.LOW)
                    ispressBT4 = True
                    time.sleep(0.5)
                    continue
        # den sang nhap nhay khi bam BT3
        if ispressBT3:
            print("Durring Blinking")
            if GPIO.input(LED) == GPIO.LOW:
                GPIO.output(LED, GPIO.HIGH)
                time.sleep(1)
            if GPIO.input(LED) == GPIO.HIGH:
                GPIO.output(LED, GPIO.LOW)
                time.sleep(1)
try:
    main() #goi ham
except KeyboardInterrupt: #xu li su kien Ctrl + C
    GPIO.cleanup() #giai phong GPIO
        
    

