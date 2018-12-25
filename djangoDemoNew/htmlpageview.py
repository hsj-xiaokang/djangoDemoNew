#!/usr/bin/env python
# encoding: utf-8
'''
@author: heshengjin-何胜金
@contact: 2356899074@qq.com
@software: pycharm
@file: htmlpageview.py
@time: 2018/12/25 13:20
@desc:html页面返回测试
'''

from django.shortcuts import render


# 路由中指定要调用的函数,传入一个用户请求参数
def getHtmlIndex(request):
    # 返回HTML页面时,使用render来渲染和打包
    return render(request, 'index.html')