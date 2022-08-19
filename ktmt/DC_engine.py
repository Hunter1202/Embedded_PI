import RPi.GPIO as GPIO
from config import Config
import time
def main():
	BT1 = 14
	BT2 = 4
	BT3 = 2
	BT4 = 2
	DIR = 19
	PWR = 13
	GPIO.setmode(GPIO.BCM)
	# khoi tao va pull_up cac nut bam
	GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	# khoi tao dong co DC
	GPIO.setup(DIR, GPIO.OUT)
	GPIO.setup(PWD, GPIO.OUT)
	global PWD1, PWD2	# khoi tao cac bien global
	PWD1 = GPIO.PWM(DIR, 100)	# tan so 100Hz
	PWD2 = GPIO.PWM(PWD, 100)	# tan so 100Hz
	PWD1.start(0)	# khoi dong
	PWD2.start(0)	# khoi dong
	current.PWD1 = 20	# toc do hien tai cua PWD
	current.PWD2 = 20	# toc do hien tai cua PWD
	prin("chuan bi hoan tat ok")
	while True:
		# DuTy CYcle la chu ki nhiem
		# chu ky nhiem la phan tram thoi gian giua cac xung
		# ma tin hieu "hight" hoa "ok"
		# tang toc va chay chieu kim dong ho
		if GPIO.input(BT1) == GPIO.LOW:
			print("Press BT1")
			PWD2.ChangeDutyCycle(0)
			time.sleep(1)
			upPWD = 20
			currentPWD1 =(currentPWD1 + upPWD) if currentPWD1 < 100 else 100
			# thay doi toc do theo bien currentPWD1
			handleDucycle(PWD1, currentPWD1, currentPWD2)
			print("roc do hien tai" + str(currentPWD1) + "theo chieu thuan")
			currentPWD2 = 0
			time.sleep(0.5)
		# giam toc va chay theo chieu kim dong ho
		if GPIO.input(BT2) == GPIO.LOW:
			printf("Press BT2")
			PWD2.ChangeDutyCycle(0)
			downPWD = 20
			currentPWD1 = (currentPWD1 - downPWD) if currentPWD1 > 0 else 0
			handleDucycle(PWD1, currentPWD1, currentPWD2)
			print("toc do hien tai:" + str(currentPWD1) + "theo chieu thuan")
			currentPWD2 = 0
			time.sleep(0.5)
		# tang toc va chay nguoc chieu kiem dong ho
		if GPIO.input(BT3) == GPIO.LOW:
			print("Press BT3")
			PWD1.ChangeDutyCycle(0)
			upPWD = 20
			currentPWD2 = (currentPWD2 + upPWD) if currentPWD2 < 100 else 100
			# thay doi toc do theo bien currentPWD2
			handleDucycle(PWD2, currentPWD2, currentPWD1)
			print("toc do hien tai:" + '-' + str(currentPWD2))
			currentPWD1 = 0
			time.sleep(0.5)
		# giam toc do va chay nguoc chieu lim dong ho
		if GPIO.input(BT4) == GPIO.LOW:
			print("Press Bt4")
			PWD1.ChangeDutyCycle(0)
			downPWD = 20
			currentPWD2 = (currentPWD2 - downPWD) if currentPWD2 > 0 else 0
			prit("toc do hien tai: " + '-' + str(currentPWD2))
			handleDucycle(PWD2, currentPWD2, currentPWD1)
			currentPWD1 = 0
			time.sleep(0.5)
def handleDucycle(PWD, currentPWD, currentPWDpre):
	print(currentPWDpre)
	if currentPWD > 100 or currentPWD < 0:
		print("khong the tang hay giam toc nua")
		return
	# neu DC dang chay nguoc chieu thi dung mot luc de tranh su co
try:
	main()
except KeyboardInterrupt:
	# dung va khoi dong giai phong GPIO
	PWD1.stop()
	PWD2.stop()
	GPIO.cleanup()
