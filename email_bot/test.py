import threading
import time
import random
import yagmail
import requests

#  通过邮箱服务器登录自己的邮箱
email = yagmail.SMTP(user="sunnyajie@163.com", password="5201314asd", host='smtp.163.com')

def get_news():
	#  天行数据 段子http://api.tianapi.com/txapi/mnpara/index?key=eb62e0a34b2b7269b4de1d936e05e22d
	url = "http://api.tianapi.com/txapi/mnpara/index?key=eb62e0a34b2b7269b4de1d936e05e22d"
	res = requests.post(url)
	result = res.json()['newslist'][0]['content']

	return result

# 蝶宝，我，何翔，老猫，
# 衮毅，欧阳，李聪，弟弟波
# 宝，
# receivers = ['2640360179@qq.com', '1571858518@qq.com',  '1175376884@qq.com', '1941467179@qq.com',
# 			'2761118029@qq.com', '1627466272@qq.com', '1021062833@qq.com', '2211946606@qq.com',
# 			 '1912963948@qq.com', ]

receivers = ['1571858518@qq.com']

#  邮件发送器
class sender(threading.Thread):
	def run(self):
		while True:
			text = get_news()
			contents = [text, './12.png', './12.png']
			print(contents)

			# 发送邮件
			# email.send(receivers, '阿杰的每天一段', contents)

			# 每天发送
			ran_int = random.randint(0, 2000) - 1000
			# 一天后在发送
			time.sleep(86400 + ran_int)


send = sender()
send.start()

