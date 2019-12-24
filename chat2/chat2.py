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
		slow_print("系统提示：想要打开输入框需重启此软件...")
		window.destroy()


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
	url = host + "?id=1&operation=r"
	try:
		res = requests.get(url)
	except:
		print("出现网络错误!")

	msg = res.text
	# print("内容是"+msg+"muji")
	if msg != "":
		content = "Ta：" + msg
		slow_print(content, 0.1)


#  发送消息
def write_data(content):
	url = host + "?id=1&operation=w&content=" + content
	try:
		res = requests.get(url)
	except:
		print("出现网络错误!")

	if res.text == "ok":
		msg = "我：" + content
		slow_print(msg, 0.1)


# 实现慢输出
def slow_print(print_string, sleep_time=0.1):
	for char in print_string:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(sleep_time)
	print()


# 开启线程监听新消息
class ListeningData(threading.Thread):
	def run(self):
		while True:
			get_data()
			time.sleep(0.5)


if __name__ == "__main__":
	slow_print("主人您已上线！！！")
	print()
	listener = ListeningData()
	listener.start()
	window.mainloop()



