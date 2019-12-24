import requests
import random
from bs4 import BeautifulSoup

url = 'http://www.weather.com.cn/weather1d/101220101.shtml'  #数据地址,从浏览器copy
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3226.400 QQBrowser/9.6.11681.400'
}

timeout = random.choice(range(80, 180))  # 超时时间
req = requests.get(url, headers=header, timeout=timeout)
req.encoding = 'utf-8'  # 防止中文乱码
code = req.status_code  # 返回状态,200代表OK
# print(code)

soup = BeautifulSoup(req.text, 'html.parser')
# 分析
print(soup)
ul_tag = soup.find_all('div', '.tem') # 利用 css 查找
# ul_tag = soup.select('.tem')  # 利用 css 查找

print(ul_tag) #取出七天数据


# 打印每一天数据
