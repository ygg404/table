# -*- coding: utf-8 -*-
import configparser
import os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )
SYS_DIR = os.path.join(os.path.join(BASE_DIR,'Conf'),'sys.conf')

class Config():
	@staticmethod
	def getSysValue(key):
		try:
			cf = configparser.ConfigParser()
			cf.read(SYS_DIR , encoding='UTF-8')
			return cf.get("sys", key)
		except Exception as e:
			raise e

	@staticmethod
	def setSysValue(key ,value):
		try:
			cf = configparser.ConfigParser()
			cf.read(SYS_DIR , encoding='UTF-8')
			cf.set("sys", key ,value)
			with open(SYS_DIR, "w") as fw:
				cf.write(fw) # 使用write将修改内容写到文件中，替换原来config文件中内容
		except Exception as e:
			raise e


if __name__ == "__main__":
	try:
		print ( Config.setSysValue("SystemToMail" , "false") )
	except Exception as e:
		print (e)