from enum import Enum,unique

"""登录类型"""
@unique
class OperationType(Enum):
    #"其他"
    Other = 0
    #("登录")
    Login = 1
    #("退出")
    Exit = 2
    #("访问")
    Visit = 3
    #("离开")
    Leave = 4
    #("新增")
    Create = 5
    #("删除")
    Delete = 6
    #("修改")
    Update = 7
    #("提交")
    Submit = 8
    #("异常")
    Exception = 9
    #("移动登录")
    AppLogin = 10

if  __name__ == '__main__':
    print( OperationType.AppLogin.value)