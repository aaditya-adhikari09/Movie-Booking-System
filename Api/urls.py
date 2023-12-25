from django.contrib import admin 
from django.urls import path ,include
from rest_framework import routers
from Api.views import UserViewSet , ExperienceViewSet

router =routers.DefaultRouter()
router.register(r"user",UserViewSet)
router.register(r"experience",ExperienceViewSet)




urlpatterns =[
    path("",include(router.urls)) ,
]