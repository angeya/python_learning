import requests
import sys
import time
import threading

host = "http://47.107.173.24/chat"
# 获取消息


def get_data():
	url = host + "?id=1&operation=r"
	try:
		res = requests.get(url)
	except:
		print("出现网络错误!")

	msg = res.text
	# print("内容是"+msg+"muji")
	if msg != "":
		content = "客服08163黄蝶蝶：" + msg
		slow_print(content, 0.1)

#  发送消息
def write_data(content):
	url = host + "?id=1&operation=w&content=" + content
	try:
		res = requests.get(url)
	except:
		print("出现网络错误!")

	if res.text == "ok":
		msg = "华米科技CTO：" + content
		slow_print(msg, 0.1)


def slow_print(print_string, sleep_time=0.1):
	for char in print_string:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(sleep_time)
	print()


class ListeningData(threading.Thread):
	def run(self):
		while True:
			get_data()
			time.sleep(0.5)


if __name__ == "__main__":
	slow_print("华米CTO已经上线！")
	print()
	listener = ListeningData()
	listener.start()
	while True:
		my_msg = input()
		write_data(my_msg)
		print()


