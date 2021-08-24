"""StudentManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from app01 import views, teacher, students

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^classes/', views.classes),
    re_path(r'^add_class/', views.add_class),
    re_path(r'^modal_add_class/', views.modal_add_class),
    re_path(r'^del_class/', views.del_class),
    re_path(r'^modal_del_class/', views.modal_del_class),
    re_path(r'^edit_class/', views.edit_class),
    re_path(r'^modal_edit_class/', views.modal_edit_class),

    re_path(r'^teacher/', teacher.findteacher),
    re_path(r'^add_teacher/', teacher.add_teacher),
    re_path(r'^del_teacher/', teacher.del_teacher),
    # re_path(r'^edit_teacher/', teacher.edit_teacher),

    re_path(r'^students/', students.findstudent),
    re_path(r'^add_student/', students.add_student),
    re_path(r'^modal_add_student/', students.modal_add_student),
    re_path(r'^del_student/', students.del_student),
    re_path(r'^modal_del_student/', students.modal_del_student),
    re_path(r'^edit_student/', students.edit_student),
    re_path(r'^modal_edit_student/', students.modal_edit_student),

    re_path(r'^teachers/', teacher.teachers),
    re_path(r'^add_teacherclass/', teacher.add_teacherclass),
    re_path(r'^modal_add_teacherclass/', teacher.modal_add_teacherclass),
    re_path(r'^get_all_class', teacher.get_all_class),
    re_path(r'^edit_teacherclass/', teacher.edit_teacherclass),

]
