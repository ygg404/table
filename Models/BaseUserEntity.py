from django.db import models

class BaseUser(models.Model):
    userid = models.CharField(db_column='UserId', primary_key=True, max_length=50)  # Field name made lowercase.
    encode = models.CharField(db_column='EnCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50, blank=True, null=True)  # Field name made lowercase.
    secretkey = models.CharField(db_column='Secretkey', max_length=50, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='RealName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='NickName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headicon = models.CharField(db_column='HeadIcon', max_length=200, blank=True, null=True)  # Field name made lowercase.
    quickquery = models.CharField(db_column='QuickQuery', max_length=200, blank=True, null=True)  # Field name made lowercase.
    simplespelling = models.CharField(db_column='SimpleSpelling', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateTimeField(db_column='Birthday', blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='Telephone', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    oicq = models.CharField(db_column='OICQ', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wechat = models.CharField(db_column='WeChat', max_length=50, blank=True, null=True)  # Field name made lowercase.
    msn = models.CharField(db_column='MSN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    managerid = models.CharField(db_column='ManagerId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=50, blank=True, null=True)  # Field name made lowercase.
    organizeid = models.CharField(db_column='OrganizeId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DepartmentId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    roleid = models.CharField(db_column='RoleId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dutyid = models.CharField(db_column='DutyId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dutyname = models.CharField(db_column='DutyName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    postid = models.CharField(db_column='PostId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    workgroupid = models.CharField(db_column='WorkGroupId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    securitylevel = models.IntegerField(db_column='SecurityLevel', blank=True, null=True)  # Field name made lowercase.
    useronline = models.IntegerField(db_column='UserOnLine', blank=True, null=True)  # Field name made lowercase.
    openid = models.IntegerField(db_column='OpenId', blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='Question', max_length=50, blank=True, null=True)  # Field name made lowercase.
    answerquestion = models.CharField(db_column='AnswerQuestion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    checkonline = models.IntegerField(db_column='CheckOnLine', blank=True, null=True)  # Field name made lowercase.
    allowstarttime = models.DateTimeField(db_column='AllowStartTime', blank=True, null=True)  # Field name made lowercase.
    allowendtime = models.DateTimeField(db_column='AllowEndTime', blank=True, null=True)  # Field name made lowercase.
    lockstartdate = models.DateTimeField(db_column='LockStartDate', blank=True, null=True)  # Field name made lowercase.
    lockenddate = models.DateTimeField(db_column='LockEndDate', blank=True, null=True)  # Field name made lowercase.
    firstvisit = models.DateTimeField(db_column='FirstVisit', blank=True, null=True)  # Field name made lowercase.
    previousvisit = models.DateTimeField(db_column='PreviousVisit', blank=True, null=True)  # Field name made lowercase.
    lastvisit = models.DateTimeField(db_column='LastVisit', blank=True, null=True)  # Field name made lowercase.
    logoncount = models.IntegerField(db_column='LogOnCount', blank=True, null=True)  # Field name made lowercase.
    sortcode = models.IntegerField(db_column='SortCode', blank=True, null=True)  # Field name made lowercase.
    deletemark = models.IntegerField(db_column='DeleteMark', blank=True, null=True)  # Field name made lowercase.
    enabledmark = models.IntegerField(db_column='EnabledMark', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    createuserid = models.CharField(db_column='CreateUserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    createusername = models.CharField(db_column='CreateUserName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifydate = models.DateTimeField(db_column='ModifyDate', blank=True, null=True)  # Field name made lowercase.
    modifyuserid = models.CharField(db_column='ModifyUserId', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifyusername = models.CharField(db_column='ModifyUserName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'base_user'
