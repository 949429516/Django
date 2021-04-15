from django.shortcuts import render, redirect
from .SqlManager import *


db = dbManager()


def findstudent(request):
    sql = "select student.id, student.name, class.title from student left join class on student.class_id = class.id"
    students_list = db.findmany(sql)
    return render(request, 'students.html', {"students_list": students_list})


def add_student(request):
    if request.method == "GET":
        sql_find = "select id, title from class;"
        class_list = db.findmany(sql_find)
        return render(request, "add_student.html", {"class_list": class_list})
    else:
        name = request.POST.get("name")
        class_id = request.POST.get("class_id")
        sql = "insert into student (name, class_id) values ('{}','{}')".format(name, class_id);
        db.commit(sql)
        return redirect('/students/')

