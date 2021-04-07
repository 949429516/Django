"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from django.shortcuts import HttpResponse, render, redirect
from .mydatabase import mysqlpython

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        #用户提交的数据(请求体里的数据)
        u = request.POST.get('username')
        p = request.POST.get('password')
        if u == "root" and p == '123123':
            return redirect("/index/")
        else:
            #登陆失败
            return render(request, "login.html", {'msg': "傻屄"})

def index(request):
    A = mysqlpython()
    return render(request,
                  'index.html',
                  {"name": "fuck",
                   "users": ["尼玛", "泥巴"],
                   "user_dict": {"k1": "v1", "k2": "v2"},
                   "user_list_dict": A.find()
                   })


def Delete(request):
    id = request.GET.get('nid')
    A = mysqlpython()
    A.Del(id)
    return render(request,
                  'index.html',
                  {"name": "fuck",
                   "users": ["尼玛", "泥巴"],
                   "user_dict": {"k1": "v1", "k2": "v2"},
                   "user_list_dict": A.find()
                   })


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'login/', login),
    re_path(r'^index/$', index),
    url(r'^del/$', Delete),
]
