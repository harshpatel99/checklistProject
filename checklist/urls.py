from django.urls import path
from django.urls.conf import re_path

from . import views

urlpatterns = [
    path('', views.checkList)
]
