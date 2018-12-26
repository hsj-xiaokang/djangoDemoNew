# -*- coding: utf-8 -*-
from datetime import date,datetime


from django.shortcuts import render,redirect
from booktest.models import BookInfo
#导入`connection`
from django.db import connection


# 查询所有图书并显示的视图函数
def index(request):
    books=BookInfo.objects.all()
    selectAll()
    return render(request,u'booktest/index.html',{'books':books})

# 新增图书视图视图函数
def addBook(request):
    book=BookInfo()
    book.btitle=u'mysql操作_auto_自动_lby'
    book.bpub_date=datetime.now()
    book.save()
    # return HttpResponse('ok')
    # sql操作
    addBookSql()
    # 重定向跳转到首页
    return redirect(u'/index/')

# 根据图书id删除一本书的视图函数
def delBook(request):
    # 获取url
    p = request.path.split(ur'/')[-1]
    print p
    # 查询出图书
    b=BookInfo.objects.get(id=int(p))
    b.delete()
    return redirect(u'/index/')

 # insert
def addBookSql():
    cursor = connection.cursor()
    #要想使用sql原生语句，必须用到execute()函数
    #然后在里面写入sql原生语句
    cursor.execute("insert into booktest_bookinfo(btitle,bread,bcomment,idDelete) values ('btitle-sql' ,1,1,1)")
    return redirect(u'/index/')

# select
def selectAll():
    cursor = connection.cursor()
    cursor.execute("select * from booktest_bookinfo")
    #使用一个变量来接收查询到的数据，
    #fetchall（）返回查询到的所有数据
    rows = cursor.fetchall()

    for row in rows:
        print(row)


