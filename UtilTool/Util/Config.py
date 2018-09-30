# -*- coding: utf-8 -*-
import configparser
import os

BASE_DIR =os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) )

class Config():
	@staticmethod
	def getSysValue(key):
		path = os.path.join(os.path.join(BASE_DIR,'Conf'),'sys.conf')
		cf = configparser.ConfigParser()
		cf.read(path , encoding='UTF-8')
		return cf.get("sys", key)



if __name__ == "__main__":
	print ( Config.getSysValue("UserName") )