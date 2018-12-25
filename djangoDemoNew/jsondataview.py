#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: jsondataview.py
@time: 2018/12/25 13:16
@desc:json测试
'''

import json
from django.http import HttpResponse


def getJson(request):
    resp = {'errorcode': 100, 'detail': 'Get success','data':ur'json测试'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
