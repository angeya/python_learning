import requests
import sys
import time
url = "http://127.0.0.1:5000/"


def slow_print(string):
	for i in string:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(0.1)
	print()


while True:
	slow_print("请输入需要发送的图片的路径")
	image = input()
	image_file = "./" + image
	try:
		img = open(image_file, 'rb').read()
	except:
		slow_print("该图片不存在，请重新输入")
	else:
		files = {'img': ('hi.jpg', img, "image/png")}
		res = requests.post(url=url, files=files)
		print(res.text)
