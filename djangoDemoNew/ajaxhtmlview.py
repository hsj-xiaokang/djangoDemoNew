#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: ajaxhtmlview.py
@time: 2018/12/25 14:59
@desc:ajax测试
'''
import json
from django.http import HttpResponse
from django.shortcuts import render


# 路由中指定要调用的函数,传入一个用户请求参数
def getAjaxIndex(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, u'ajaxindex.html')

# 表单提交调用的函数post
def getAjaxPost(request):
    # 相当于Java的Servlet中的doPost情况
    if request.method == 'POST':
        # 获取表单提交来的数据
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 在控制台输出表单的提交看一下
        print(username, password)
        # 将这些数据打包成字典
        tempDic = {'usr': username, 'pwd': password}
    return HttpResponse(json.dumps(tempDic), content_type="application/json")

# 表单提交调用的函数get
def getAjaxGet(request):
    # 相当于Java的Servlet中的doPost情况
    if request.method == 'GET':
        # 获取表单提交来的数据
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
        # 在控制台输出表单的提交看一下
        print(username, password)
        # 将这些数据打包成字典
        tempDic = {'usr': username, 'pwd': password}
    return HttpResponse(json.dumps(tempDic), content_type="application/json")