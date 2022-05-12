# -*- coding: utf-8 -*-
# @Time    : 2022/5/12 3:22 下午
# @Author  : rabbit
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path
from verification import views
app_name = 'verification'
urlpatterns = [
    path('pics/<uuid:img_codes>/', views.ImageCode.as_view(), name='register'),
]