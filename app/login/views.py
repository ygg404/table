from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

"""视图"""
def index(request):
    return render(request, "logon/login.html")

"""登录验证"""
def checklogin(request):
     return render(request, "logon/login.html")