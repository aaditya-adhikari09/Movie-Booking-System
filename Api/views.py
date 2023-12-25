from django.shortcuts import render 
from django.http import JsonResponse
from .models import User , Experience
from .serializer import UserSerializer, ExperienceSerializer 
from rest_framework import viewsets
from rest_framework.decorators import action 
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset =User.objects.all()
    serializer_class = UserSerializer
# user/{userId}/user

@action(detail = True, methods=['get'])

class ExperienceViewSet(viewsets.ModelViewSet):
     queryset = Experience.objects.all()
     serializer_class=ExperienceSerializer