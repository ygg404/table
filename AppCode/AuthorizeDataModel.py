"""用户数据权限"""
class AuthorizeDataModel(object):
    def __init__(self):
        #功能模块主键
        self.ModuleId = []
        #获得有权限的数据列表SQL语句
        self.ReadAutorize =[]
        # 可读用户ID
        self.ReadAutorizeUserId=[]
        # 可写数据权限SQL语句
        self.WriteAutorize =[]
        # 可写数据权限
        self.WriteAutorizeUserId=[]