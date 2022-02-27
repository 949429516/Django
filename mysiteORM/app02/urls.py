from django.urls import re_path
from app02 import views, csrf
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    re_path(r'^test/$', views.test),
    re_path(r'^index/$', views.index, name='name1'),
    re_path(r'^custom/$', views.custom, name='custom'),
    # re_path(r'^csrf/$', csrf.csrf1, name='csrf'),
    re_path(r'^csrf/$', csrf.Foo.as_view(), name='csrf'),
    # url中添加装饰器
    # re_path(r'^csrf/$', csrf_exempt(csrf.Foo.as_view()), name='csrf'),

]
