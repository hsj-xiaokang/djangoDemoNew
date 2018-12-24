#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: view.py
@time: 2018/12/24 12:39
@desc:view.py
'''
from django.http import HttpResponse
from django.http import HttpRequest


def hello(HttpRequest):
    print HttpRequest
    return HttpResponse(ur"Hello world-heshengjin-何胜金")
