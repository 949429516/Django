from django.shortcuts import render, redirect
from .SqlManager import dbManager

db = dbManager()

def findteacher(request):
    sql = "select id, name from teacher"
    data_list = db.findmany(sql_find=sql)
    return render(request, "teacher.html", {"data_list": data_list})


def add_teacher(request):
    if request.method == "GET":
        return render(request, "add_teacher.html")
    else:
        name = request.POST.get("name")
        sql = "insert into teacher (name) values ('{}')".format(name)
        db.commit(sql)
        return redirect("/teacher/")


def del_teacher(request):
    nid = request.GET.get("nid")
    sql = "delete from teacher where id = {}".format(nid)
    db.commit(sql)
    return redirect("/teacher/")


def edit_teacher(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        sql = "select id, name from teacher where id = {};".format(nid)
        data_list = db.findone(sql)
        return render(request, 'edit_teacher.html', {'data_list': data_list})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        sql = "update teacher set name = '{}' where id = {};".format(name, nid)
        print(sql)
        db.commit(sql)
        return redirect("/teacher/")