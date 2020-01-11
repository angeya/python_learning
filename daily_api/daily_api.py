import requests


# 随机头像生成
def get_img(i):
	url = "https://api.uomg.com/api/rand.avatar"
	response = requests.get(url)
	f = open("./hi" + str(i) + ".jpg", "wb")
	f.write(response.content)
	f.close()

for i in range(10):
	get_img(i)


# url = "http://route.showapi.com/107-32"
# response = requests.get(url)
# result = response.json()
# print(result)