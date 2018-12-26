#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: authview.py
@time: 2018/12/25 15:39
@desc:登录权限(权限相关操作):https://www.cnblogs.com/ccorz/p/6358074.html

数据库mysql：
      第一步：djangoDemoNew/__init__.py里面添加代码：
             pymysql.install_as_MySQLdb()--先安装pymysql
      第二步：https://blog.csdn.net/u014745194/article/details/73801625
'''
from django.contrib.auth.models import User
from django.shortcuts import render
import json
from django.http import HttpResponse
#导入`connection`
from django.db import connection
from booktest.models import UserMoreInfo
import random
from datetime import date,datetime

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# 路由中指定要调用的函数,传入一个用户请求参数
def getAuthIndex(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, u'authindex.html')

# 创建用户
def createAuthUser(request):
    if request.method == 'POST':
        # 获取表单提交来的数据
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        # auth_user
        user = User.objects.create_user(username,email, password)
        user.save()

        # exclude(username='%s' % (username))
        # userback = list(User.objects.filter(username='%s' % (username)) )
        # for a in userback:
        #     print a
        cursor = connection.cursor()
        cursor.execute("select * from auth_user where username = '%s'" % (username))
        # 使用一个变量来接收查询到的数据，
        # fetchall（）返回查询到的所有数据tuple
        rows = cursor.fetchall()
        for row in rows:
            # id
            print(row[0])
            umf = UserMoreInfo()
            umf.userId = row[0]
            umf.create_date = datetime.now()
            umf.nikename = random.random()
            umf.save()

    resp = {'errorcode': 1, 'detail': 'success', 'data': ur'创建auth_user成功[%s]' % (username)}
    return HttpResponse(json.dumps(resp), content_type="application/json")


# 登录
def loginOp(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            resp = {'errorcode': 1, 'detail': 'success', 'data': ur'登录成功[%s]' % (username)}
            return HttpResponse(json.dumps(resp), content_type="application/json")
    resp = {'errorcode': 0, 'detail': 'fail', 'data': ur'登录失败[%s]' % (username)}
    return HttpResponse(json.dumps(resp), content_type="application/json")

#登出
def logoutOp(request):
    try:
        logout(request)
    except Exception,e:
        resp = {'errorcode': 0, 'detail': 'fail', 'data': ur'登出失败啦'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    resp = {'errorcode': 1, 'detail': 'success', 'data': ur'登出成功了'}
    return HttpResponse(json.dumps(resp), content_type="application/json")

# 测试登录才能访问的资源
@login_required(login_url='/hello')
def loginCanAccess(request):
    print '--------------coming-------------------'
    resp = {'errorcode': 1, 'detail': 'success', 'data': ur'测试登录才能访问的资源'}
    return HttpResponse(json.dumps(resp), content_type="application/json")