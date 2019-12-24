import time
from selenium import webdriver


url = "http://10.2.5.251/"
account = "08163180"
password = "120133"

web = webdriver.Chrome()
web.implicitly_wait(5)
web.get(url)

#  判断是否已经登录过
if web.title == "注销页":
	print("您已经成功登录！")

else:
	web.implicitly_wait(1)
	web.find_element_by_xpath("//input[@placeholder='学号']") .send_keys(account)
	web.find_element_by_xpath("//input[@placeholder='密码']") .send_keys(password)
	web.find_element_by_xpath("//option[@value='@unicom']").click()
	# web.find_element_by_xpath("//input[@value='登录']").click()

	element = web.find_element_by_xpath("//input[@value='登录']")
	web.execute_script("arguments[0].click();", element)
	# 有的按钮无法直接click，就是用如下方法
	# element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
	# driver.execute_script("arguments[0].click();", element)

#  登录成功之后，关闭浏览器
web.close()
print("this program is made by angeya")

