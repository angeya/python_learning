from __future__ import print_function
import shutil
import time
import say_hello as s
import ctypes, sys


def is_admin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False
#  只有从本程序开始的时候，main方法才会被执行，被当做模块调用的时候。main方法不执行
if __name__=='__main__':

	if is_admin():
		# 将要运行的代码加到这里
		try:
			shutil.copyfile("./hi.txt", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\hi.txt")

		except Exception as e:
			print("复制失败！")
			print(e)
		else:
			print("复制成功！")

	else:
		if sys.version_info[0] == 3:
			ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
		# else:  # in python2.x
			# ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)






