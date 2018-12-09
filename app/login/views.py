from django.shortcuts import render
import Models.BaseArea.models as mba

"""视图"""
def index(request):
    return render(request, "logon/login.html")

"""登录验证"""
def CheckLogin(request):
    entity = mba.BaseArea()
    return render(request, "logon/login.html")