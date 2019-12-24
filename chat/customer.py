import requests
import sys
import time
import threading
import easygui


host = "http://127.0.0.1/chat"
# 获取消息
def get_data():
	msg = ""
	url = host + "?id=2&operation=r"
	try:
		res = requests.get(url)
	except:
		print("出现网络错误!")

	else:
		msg = res.text
	# print("内容是"+msg+"muji")
	if msg != "":
		content = "华米科技CTO：" + msg
		slow_print(content)


#  发送消息
def write_data(content):
	url = host + "?id=2&operation=w&content=" + content
	try:
		res = requests.get(url)
	except:
		print("出现网络错误!")

	if res.text == "ok":
		msg = "我：" + content
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


# 输入消息框
def input_box():
	my_msg = easygui.enterbox("在这里输入你的信息")
	return my_msg


if __name__ == "__main__":
	slow_print("欢迎使用安杰聊天终端 版本号1.1.2")
	print()

	listener = ListeningData()
	listener.start()
	slow_print("您已成功上线！开始聊天吧...")
	print()
	while True:
		my_msg = input_box()
		if my_msg == None:
			break
		write_data(my_msg)
		print()


