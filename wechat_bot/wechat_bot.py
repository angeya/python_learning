# coding:utf-8
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests
from bs4 import BeautifulSoup
import time
import random

# bot = Bot()


# linux执行登陆请调用下面的这句
# bot = Bot(console_qr=2, cache_path="botoo.pkl")

# def get_news():
# 	"""获取金山词霸每日一句，英文和翻译"""
# 	url = "http://open.iciba.com/dsapi/"
# 	r = requests.get(url)
# 	content = r.json()['content']
# 	note = r.json()['note']
# 	return content, note

def get_req():
	req = requests.get("https://m.tianqi.com/hefei/")
	# req.encoding = "utf8"
	soup = BeautifulSoup(req.text, 'html.parser')
	# print(soup)
	# print(req.text)
	city = soup.select(".hhx_index_newHead_l")[0].text + "市"
	date_array = soup.select(".date")[0].text.split()
	date = date_array[0][5:]+" "+date_array[1]+" "+time.strftime("%H:%M", time.localtime())
	temp = soup.select(".temp .txt")[0].text
	now = soup.select(".now")[0].text
	air = "空气质量 "+soup.select(".info .b1")[0].text.replace(' ', '')
	wet = soup.select(".info .b2")[0].text.replace(' ', '')
	wind = soup.select(".info .b3")[0].text.replace(' ', '')
	content = "【安杰天气提醒】\n"+date+"\n"+city+" "+temp+" | "+now+"\n"+air+" "+wet+" "+wind
	print(content)
	# return content
def send_news():
	try:
		content = get_req()
		# 你朋友的微信名称，不是备注，也不是微信帐号。
		# my_friend = bot.friends().search('黄蝶蝶')[0]
		# my_friend.send(content)
		# 每18000秒（3小时），发送1次
		# t = Timer(18000, send_news)
		# 为了防止时间太固定，于是决定对其加上随机数
		ran_int = random.randint(0, 1800)
		t = Timer(18000 + ran_int, send_news)
		# t = Timer(10, send_news)
		t.start()
	except:
		# 微信昵称。
		# my_friend = bot.friends().search('画诗')[0]
		# my_friend.send(u"今天消息发送失败了")
		print("失败咯")


if __name__ == "__main__":
	# send_news()
	get_req()