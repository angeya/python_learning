import sys
import time
import os
import requests
import pygame
import threading


class player(threading.Thread):
	def run(self):
		file = 'startup.mp3'  # 文件名是完整路径名
		pygame.mixer.init()  # 初始化音频
		pygame.mixer.music.load(file)  # 载入音乐文件
		pygame.mixer.music.play()  # 开始播放
		# time.sleep(24.5)  # 播放10秒
		# pygame.mixer.music.stop()  # 停止播放


send = player()
send.start()



string_array = [
"◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◇◆◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◇◆◆◇◇◇◆◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◆◇◇◇◇◆◆◆◇◆◆◇◇◇◇◇◇◇◇◇◇◇◆◆◆◇◇◇◇◆◆◆◇◆◆◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◇◆◆◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◆◆◇◆◆◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◆◆◇◆◆◇◆◆◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◇◇◆◇◇◇◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◇◆◆◆◆◇◆◇◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◇◆◆◆◆◇◆◇◇◇◇◇◇◇\n",
"◇◇◇◇◇◆◆◆◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◇◆◇◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◆◇◇◇◇◆◇◆◆◆◆◆◆◆◆◇◇◇\n",
"◇◇◇◇◇◆◆◆◆◆◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◆◇◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◆◆◇◆◇◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◇◇◆◇◇◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◆◆◆◆◆◆◆◆◆◇◆◇◆◆◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◆◆◆◇◆◇◆◆◇◇◇◇◇◇◇\n",
"◇◇◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◆◆◆◆◆◆◇◇◆◇◆◆◆◆◆◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◇◇◆◇◆◆◆◆◆◇◇◇◇◇◇\n",
"◇◇◇◆◆◆◆◆◇◇◇◆◇◇◇◆◆◆◇◇◇◇◇◇◇◇◇◇◆◇◆◇◆◇◇◆◇◆◆◇◇◇◆◇◇◇◇◇◇◇◇◇◆◇◆◇◆◇◇◆◇◆◆◇◇◇◆◇◇◇◇◇\n",
"◇◇◇◇◇◇◆◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◆◇◆◆◆◇◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◆◇◆◆◆◇◆◆◆◆◆◆◆◆◆◇◇◇◇◇\n",
"◇◇◇◇◇◇◆◆◆◆◆◆◆◆◇◆◆◇◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◇◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◇◆◆◆◆◆◆◇◇◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◆◇◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◆◆◆◇◇◇◇◇◇◇◆◆◆◆◆◆◇◇◇◇◇◇◇◇◆◆◆◇◇◇◇◇◇◇◆◆◆◆◆◆◇◇◇◇\n",
"◇◇◇◇◇◇◇◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◆◇◆◆◆◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◆◇◆◆◆◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇\n",
"◇◇◇◇◇◇◇◆◇◇◇◆◇◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◆◆◆◆◆◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◇◆◆◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◆◇◆◆◆◆◆◆◇◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◆◆◆◆◆◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◆◆◆◆◆◇◆◆◆◆◆◇◆◇◆◆◇◇◇◇◇◇◇◇◆◆◆◆◆◇◆◆◆◆◆◇◆◇◆◆◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◆◆◆◆◇◇◆◆◆◆◇◇◇◇◇◇◇◇◇◇◆◆◇◇◇◇◆◆◆◇◇◆◇◆◆◆◆◇◇◇◇◇◇◇◆◆◇◇◇◇◆◆◆◇◇◆◇◆◆◆◆◇◇◇◇\n",
"◇◇◇◇◇◇◇◆◆◆◆◇◇◇◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◆◇◇◆◆◇◇◆◆◆◆◇◇◇◇◇◇◇◇◇◇◇◆◆◆◇◇◆◆◇◇◆◆◆◆◇◇◇\n",
"◇◇◇◇◇◆◆◆◆◇◇◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇\n",
"◇◇◇◆◆◆◆◇◇◇◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◆◇◇◇◇◇◇◇◇◇\n",
"◇◇◇◆◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◆◇◇◇◇◇◇◇◇◇\n",
"◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇\n",
]

#  慢打印
def slow_print(string):
	for char in string:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.01)


def get_news():
	"""获取金山词霸每日一句，英文和翻译"""
	url = "http://open.iciba.com/dsapi/"
	try:
		res = requests.get(url, timeout=2)
		content = res.json()['content']
		note = res.json()['note']
		text = content + '\n' + note
		return text
	except:
		#  如果发生异常（没有网络连接），则返回常字符串
		return "每天都要开心哦!\n"

content = get_news()
result = "\033[1;34m" + content + "\033[0m"
print(result)

for i in string_array:
	slow_print(i)

print("\033[1;34m 输入回车关闭此窗口，输入d后回车删除此程序！ \033[0m")
key = input()
if key == "d":
	while True:
		print("\033[1;31m 确定删除吗？输入[ yes/no ] 回车确认！ \033[0m")
		affirm = input()
		if affirm == "yes":
			os.remove("./startup.mp3")
			os.remove("./heart.exe")
			break
		if affirm == "no":
			break

















#  天行数据 段子http://api.tianapi.com/txapi/mnpara/index?key=eb62e0a34b2b7269b4de1d936e05e22d
# url = "http://api.tianapi.com/txapi/mnpara/index?key=eb62e0a34b2b7269b4de1d936e05e22d"
# res = requests.post(url)
# result = res.json()['newslist'][0]['content']
# print(result)





