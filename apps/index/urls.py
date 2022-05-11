# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 10:51 上午
# @Author  : rabbit
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, re_path
from index import views
app_name = 'index'
urlpatterns = [
    path('', views.index.as_view(), name='see_index'),
    path("login/", views.Login.as_view(), name="login")
]