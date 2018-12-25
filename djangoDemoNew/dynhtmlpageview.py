#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: dynhtmlpageview.py
@time: 2018/12/25 13:32
@desc:Django模板
'''

from django.shortcuts import render


# 路由中指定要调用的函数,传入一个用户请求参数
def getDynIndex(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, u'dynindex.html')


# 存放用户输入数据的字典列表
inptDicLst = [
    # 存放一些原始数据
    {'usr': ur'字典中原来就有的用户名', 'pwd': ur'对应密码'}
]


# 表单提交调用的函数
def gosubmitdynhtml(request):
    # 相当于Java的Servlet中的doPost情况
    if request.method == 'POST':
        # 获取表单提交来的数据
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # 在控制台输出表单的提交看一下
        print(username, password)
        # 将这些数据打包成字典
        tempDic = {'usr': username, 'pwd': password}
        # 将这个字典加入到字典列表
        inptDicLst.append(tempDic)
    # 返回一个页面,如返回自己这个页面本身,第三个参数以字典方式提供数据对象
    return render(request, u'dynindex.html', {'lst': inptDicLst})