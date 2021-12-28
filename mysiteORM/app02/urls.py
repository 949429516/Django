from django.urls import re_path
from app02 import views

urlpatterns = [
    re_path(r'^test/$', views.test),
    re_path(r'^index/$', views.index, name='name1'),
    re_path(r'^custom/$', views.custom, name='custom'),
]
