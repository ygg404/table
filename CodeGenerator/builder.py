import os
import re

# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#指定表的类
def ModelsCreate(tablename):
    # 获取表 model文件
    modelsText = execCmd("cd " + BASE_DIR + "&& python manage.py inspectdb ")
    reg = 'class '+ tablename.lower() +':' + '(.*?)' + 'class'
    matchObj = re.match( r'This' , modelsText, re.I|re.M)
    print (modelsText)

ModelsCreate('baselog')