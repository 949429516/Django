import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .SqlManager import *

db = dbManager()


def findstudent(request):
    sql = "select student.id, student.name, student.class_id, class.title from student left join class on student.class_id = class.id"
    students_list = db.findmany(sql)
    sql = "select id, title from class;"
    class_list = db.findmany(sql)
    return render(request, 'students.html', {"students_list": students_list, 'class_list': class_list})


def add_student(request):
    if request.method == "GET":
        sql_find = "select id, title from class;"
        class_list = db.findmany(sql_find)
        return render(request, "add_student.html", {"class_list": class_list})
    else:
        name = request.POST.get("name")
        class_id = request.POST.get("class_id")
        sql = "insert into student (name, class_id) values ('{}','{}');".format(name, class_id)
        db.commit(sql)
        return redirect('/students/')


def modal_add_student(request):
    ret = {'status': True, 'message': None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sql = "insert into student (name, class_id) values ('{}','{}')".format(name, class_id)
        db.commit(sql)
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))


def del_student(request):
    nid = request.GET.get('nid')
    sql = "delete from student where id = {};".format(nid)
    db.commit(sql)
    return redirect('/students/')


def modal_del_student(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        print(nid)
        sql = "delete from student where id={};".format(nid)
        db.commit(sql)
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))


def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        sql = "select student.id, student.name, class.title, class_id from student left join class on student.class_id = class.id WHERE student.id = {};".format(
            nid)
        student_list = db.findone(sql)
        SqlClass = "select id, title from class;"
        class_list = db.findmany(SqlClass)
        data = {"student_list": student_list, "class_list": class_list}
        return render(request, 'edit_student.html', data)
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get("class_id")
        sql = "update student set name = '{}', class_id = {} where id = {}".format(name, class_id, nid)
        print(sql)
        db.commit(sql)
        return redirect('/students/')

def modal_edit_student(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get("class_id")
        sql = "update student set name = '{}', class_id = {} where id = {}".format(name, class_id, nid)
        db.commit(sql)
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))