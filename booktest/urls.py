#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: urls.py
@time: 2018/12/25 17:27
@desc:
'''
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^addBook/$',views.addBook),
    url(r'^delBook/[0-9]*',views.delBook)
]
