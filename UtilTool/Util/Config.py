# -*- coding: utf-8 -*-
import configparser
import os
import UtilTool.Util.BasePath as BasePath

#重写configparser 避免转化为小写
class MyConfigParser(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class Conf():
	@staticmethod
	def getSysValue(key):
		try:
			cf = configparser.ConfigParser()
			cf.read(BasePath.SYS_DIR , encoding='UTF-8')
			return cf.get("sys", key)
		except Exception as e:
			raise e

	@staticmethod
	def setSysValue(key ,value):
		try:
			cf = MyConfigParser()
			cf.read(BasePath.SYS_DIR , encoding='UTF-8')
			cf.set("sys", key ,value)
			with open(BasePath.SYS_DIR, "w") as fw:
				cf.write(fw) # 使用write将修改内容写到文件中，替换原来config文件中内容
		except Exception as e:
			raise e

	@staticmethod
	def getDbValue(key):
		try:
			cf = configparser.ConfigParser()
			cf.read(BasePath.DB_DIR , encoding='UTF-8')
			return cf.get("db", key)
		except Exception as e:
			raise e

if __name__ == "__main__":
	try:
		print ( Conf.setSysValue("SystemToMail" , "false") )
	except Exception as e:
		print (e)