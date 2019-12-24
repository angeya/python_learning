import requests
import sys
import time
import threading
import tkinter as tk
from tkinter.messagebox import askyesno

host = "http://47.107.173.24/chat"


# 获取输入框信息
def get_set_text(event):
	msg = enterbox.get()
	enterbox.delete(0, len(msg))
	write_data(msg)


# 关闭窗口警告
def close_window():
	answer = askyesno(title="提示", message="你确定要关闭此程序吗？")
	if answer:
		sys.exit()


# 定义窗口
window = tk.Tk()
window.geometry("200x60")
tk.Label(window, text="这里输入消息，回车发送").grid(row=0)
enterbox = tk.Entry(window, show=None, width=30)
enterbox.grid(row=1)

# 回车事件
enterbox.bind("<Return>", get_set_text)
window.protocol('WM_DELETE_WINDOW', close_window)


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
		content = "Ta：" + msg
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


class ListeningData(threading.Thread):
	def run(self):
		while True:
			get_data()
			time.sleep(0.5)


if __name__ == "__main__":
	slow_print("欢迎使用安杰聊天终端 版本号1.1.2")
	print()
	slow_print("您已成功上线！开始聊天吧...")
	listener = ListeningData()
	listener.start()

	print()
	window.mainloop()
	# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，
	# 如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环
	# while True:
	# 	my_msg = input()
	# 	if my_msg == None:
	# 		break
	# 	write_data(my_msg)
	# 	print()



