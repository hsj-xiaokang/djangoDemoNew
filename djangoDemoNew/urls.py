"""djangoDemoNew URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
# from django.conf.urls.defaults import *
from djangoDemoNew.view import hello
from jsondataview import getJson
from htmlpageview import getHtmlIndex
import dynhtmlpageview
import ajaxhtmlview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$', hello),
    url(r'^json/$', getJson),
    url(r'^html/$', getHtmlIndex),
    url(r'^dynhtml/$', dynhtmlpageview.getDynIndex),
    url(r'^submitdynhtml/$', dynhtmlpageview.gosubmitdynhtml),
    url(r'^getAjaxIndex/$', ajaxhtmlview.getAjaxIndex),
    url(r'^ajaxPost', ajaxhtmlview.getAjaxPost),
    url(r'^ajaxGet', ajaxhtmlview.getAjaxGet),
    url(r'^', include('booktest.urls'))
]
