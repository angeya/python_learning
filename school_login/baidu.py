import time
from selenium import webdriver

web = webdriver.Chrome()
web.implicitly_wait(5)
web.get("http://www.baidu.com")
print(web.title)
web.find_element_by_id("kw").send_keys("阿杰")
web.implicitly_wait(1)
web.find_element_by_id("su").click()
time.sleep(5)
web.close()
