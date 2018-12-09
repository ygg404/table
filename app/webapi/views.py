from django.shortcuts import render,HttpResponse
from django.core import serializers
import app.webapi.models as WebApiModels
import Models.BaseUser.models as BaseUserModels

def GetUserInfo(request):
    userlist = BaseUserModels.BaseUser.objects.all()
    userlistSerializer = WebApiModels.BaseUserSerializer(userlist)
    userlistjson = serializers.serialize("json" , userlist )
    return HttpResponse(userlistSerializer)