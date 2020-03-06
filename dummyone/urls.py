from django.conf.urls import url,include
from django.contrib import admin
import rest_framework
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from .views import StaticView
from django.conf.urls import url
from .views import *

from django.urls import path


urlpatterns = [
     path('', StaticView.as_view()),
   ]
