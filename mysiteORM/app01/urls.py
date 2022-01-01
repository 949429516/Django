from django.urls import re_path
from app01 import views

urlpatterns = [
    re_path(r'^index/(?P<a1>\d+)/$', views.index, name='name1'),
    re_path(r'^edit/(\w+)/', views.edit, name='name2'),
    re_path(r'^login/', views.login, name="m1"),
    re_path(r'^index/$', views.index1),
    # CBV方式
    re_path(r'^login.html$', views.Login.as_view(), name="cbvlogin"),
]
