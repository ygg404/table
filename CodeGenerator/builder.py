import MySQLdb
import UtilTool.Util.Config as Config
import re
import os
import chardet
import shutil


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#建立连接通道，建立连接填入（连接数据库的IP地址，端口号，用户名，密码，要操作的数据库，字符编码）
host= Config.Conf.getDbValue("host")
port= Config.Conf.getDbValue("port")
user= Config.Conf.getDbValue("user")
password=Config.Conf.getDbValue("password")
database=Config.Conf.getDbValue("database")

# cmd指令
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

#获取表得注释
def GetTableComment(tablename):
    # 打开数据库连接
    db = MySQLdb.connect(host, user, password, database, charset='utf8' )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("show table status")
    # 使用 fetchall() 方法获取所有数据
    results = cursor.fetchall()
    comment = []
    for row in results:
        if row[0].lower() == tablename.lower():
            comment = row[-1]
    cursor.close()
    return comment

#指定表的类
def ModelsText():
    # 获取表 model文件
    modelsText = execCmd("cd " + BASE_DIR + "&& python manage.py inspectdb ")
    return (modelsText)

#创建app
def AppCreate(EntityName):
    execCmd("cd " + BASE_DIR+ "\\Models" + "&& django-admin startapp " + EntityName)
    shutil.rmtree(BASE_DIR+ "\\Models\\" + EntityName +"\\migrations")
    os.remove(BASE_DIR+ "\\Models\\" + EntityName +"\\admin.py")
    os.remove(BASE_DIR+ "\\Models\\" + EntityName +"\\tests.py")
    os.remove(BASE_DIR+ "\\Models\\" + EntityName +"\\views.py")
    os.remove(BASE_DIR+ "\\Models\\" + EntityName +"\\__init__.py")

#获取表的注释
def FieldDes(tablename):
    # 打开数据库连接
    db = MySQLdb.connect(host, user, password, database, charset='utf8' )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("show FULL FIELDS from "+ tablename)
    #所有字段描述信息
    fieldDes =[]
    # 使用 fetchone() 方法获取一条数据
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        detail = row[-1]
        fieldDes.append(detail)
    cursor.close()
    return fieldDes

#创建MODEL 文件
def ModelCreate(tablename):
    fieldDes = FieldDes(tablename)
    text = ModelsText().split('\n')
    EntityName = tablename.replace('_','')
    begin = 0
    end = 0
    for index,value in enumerate(text):
        if ('class '+ EntityName+'(models.Model)').lower() in value.lower():
            begin = index
        if ('\''+tablename.lower() + '\'') in value.lower():
            end = index
    EntityName = text[begin].replace('class ','').replace('(models.Model):','')
    AppCreate(EntityName)
    fp = open(BASE_DIR + '\\Models\\' + EntityName + '\\models.py' , "w",encoding='utf8')
    fp.write("from django.db import models" +'\n'+'\n')
    fp.write('"""' + GetTableComment(tablename) + '"""\n')
    for i in range(begin,end+1):
        if i-begin != 0 and (i-begin <= len(fieldDes)):
            fp.write('    #'+ fieldDes[i-begin-1] +"\n" )
        text[i] = text[i].replace("# Field name made lowercase.","")
        #成员名 小写改为大写
        classObj = re.search("db_column='.+?'", text[i])
        if classObj != None and classObj != '':
            className = classObj.group().replace("db_column='","").replace("'","")
            text[i] = text[i].replace( className.lower() , className )
        fp.write( text[i] +'\n')
    fp.close()

#创建 serializer 文件
def SerializersCreate(tablename):
    fieldDes = FieldDes(tablename)
    text = ModelsText().split('\n')
    EntityName = tablename.replace('_','')
    begin = 0
    end = 0
    for index,value in enumerate(text):
        if ('class '+ EntityName+'(models.Model)').lower() in value.lower():
            begin = index
        if ('\''+tablename.lower() + '\'') in value.lower():
            end = index
    EntityName = text[begin].replace('class ','').replace('(models.Model):','')
    #AppCreate(EntityName)
    fp = open(BASE_DIR + '\\Models\\' + EntityName + '\\serializer.py' , "w",encoding='utf8')
    fp.write("from rest_framework import serializers" +'\n')
    modelName = EntityName + 'Model'
    fp.write("import Models." + EntityName + ".models as " + modelName + '\n' + '\n')
    fp.write('"""' + GetTableComment(tablename) + 'Serializer"""\n')
    for i in range(begin,end+1):
        if i-begin != 0 and (i-begin <= len(fieldDes)):
            fp.write('    #'+ fieldDes[i-begin-1] +"\n" )
        text[i] = text[i].replace("# Field name made lowercase.","").replace('(models.Model)','(serializers.Serializer)')
        #成员名 小写改为大写
        classObj = re.search("db_column='.+?'", text[i])
        if classObj != None and classObj != '':
            className = classObj.group().replace("db_column='","").replace("'","")
            text[i] = text[i].replace( className.lower() , className ).replace('models.' , 'serializers.')
        if 'managed' in text[i]:
            text[i] = '        ' + 'model = ' + modelName
        fp.write( text[i] +'\n')
    fp.close()

if __name__ == "__main__":
    ModelCreate('base_user')
    SerializersCreate('base_user')