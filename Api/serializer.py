from django.shortcuts import render 
from django.http import JsonResponse
from Api.models import User ,Experience
# from .serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import serializers
# Create your views here.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        fields ="__all__"

class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    id =serializers.ReadOnlyField()


    class Meta:
        model =Experience
        fields ="__all__"