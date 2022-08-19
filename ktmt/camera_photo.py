import cv2
import RPi.GPIO as GPIO
import time
def main():
    BT1 = 14
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    global namewindow
    namewindow = "Camera User"
    capture = cv2.VideoCapture(0) #khoi dong cam
    print("Capture da ok")
    while True: #neu cam dc mo
        ret, frame = capture.read() #doc video tu cam
# frame duoc tra ve la dang ma tran;
# chieu dai va chieu rong la co cua ma tran
        if GPIO.input(BT1) == GPIO.LOW:
            while True:
                
            # Hien anh ra man hinh tu bien frame
            # cv2.imshow se doc frame, chuyen frame ra dang hinh anh
                cv2.imshow("Anh chup camera", frame)
                cv2.waitKey()
                cv2.destroyWindow("Anh chup camera")
                break
try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup()
    cv2.destroyWindow(namewindow)
                
        