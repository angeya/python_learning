import requests


# 随机头像生成
# url = "https://api.uomg.com/api/rand.avatar"
# response = requests.get(url)
# f = open("./hi.jpg", "wb")
# f.write(response.content)
# f.close()
url = "http://route.showapi.com/107-32"
response = requests.get(url)
result = response.json()
print(result)