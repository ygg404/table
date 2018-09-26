import os

# execute command, and return the output
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取表 model文件
modelsText = execCmd("cd " + BASE_DIR + "&& python manage.py inspectdb ")

print (modelsText)