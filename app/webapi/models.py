from django.shortcuts import render,HttpResponse
from rest_framework import serializers
import Models.BaseUser.models as BaseUserModels

class BaseUserSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)

    class Meta:
        model = BaseUserModels.BaseUser
        fields = ('account', 'password')