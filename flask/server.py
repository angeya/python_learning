from flask import Flask, request
import time
app = Flask(__name__)


@app.route('/', methods=["POST"])
def say_hi():
	data = request.files['img']
	t = time.time()
	number = str((int(t * 10)))
	name = "./get" + number + ".jpg"
	data.save(name)
	print("文件" + name + "已经保存成功！")
	return "图片已经成功发送！"


if __name__ == "__main__":
	app.run()