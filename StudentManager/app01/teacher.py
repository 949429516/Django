import json
import time

from django.shortcuts import render, redirect, HttpResponse
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


def teachers(request):
    if request.method == "GET":
        sql = """SELECT teacher.id as tid, teacher.name, class.title FROM teacher
        LEFT JOIN relationship ON teacher.id = relationship.teacher_id
        LEFT JOIN class ON class.id = relationship.class_id;"""
        # 查询出的信息有多种重复，需要去重复将班级合并发送前台
        # [{'tid': 5, 'name': '黛里奈', 'title': ['全栈3期', '全栈2期', '全栈5期']}, {'tid': 4, 'name': '波多野结衣', 'title': ['全栈99期']}]
        data_list = db.findmany(sql)
        teacherclass_list = []
        visted = []

        while data_list:
            print(data_list)
            L = []
            data = data_list.pop()
            L.append(data['title'])
            tid = data['tid']
            if tid in visted:
                try:
                    data_list.pop()
                    continue
                except Exception:
                    pass
            visted.append(tid)
            for i in data_list:
                if i['tid'] == tid:
                    L.append(i['title'])
            data['title'] = L
            teacherclass_list.append(data)
        # print(teacherclass_list)
        return render(request, 'teacherclass.html', {'teachers_list': teacherclass_list})
    else:
        pass


def add_teacherclass(request):
    if request.method == "GET":
        sql = "SELECT id,title FROM class;"
        class_list = db.findmany(sql)
        return render(request, "add_teacherclass.html", {"class_list": class_list})
    else:
        class_list = request.POST.getlist("classid")
        teachername = request.POST.get('name')
        insertteachersql = "insert into teacher (name) values ('{}')".format(teachername)
        id = db.commit(insertteachersql)
        for item in class_list:
            relation = "INSERT INTO relationship (teacher_id,class_id) VALUES ({},{})".format(id, int(item))
            print(relation)
            db.commit(relation)
        return redirect("/teachers/")


def modal_add_teacherclass(request):
    ret = {'status': True, "message": None}
    try:
        name = request.POST.get("name")
        class_id_list = request.POST.getlist("class_id_list")
        insertteachersql = "insert into teacher (name) values ('{}')".format(name)
        id = db.commit(insertteachersql)
        for item in class_id_list:
            relationsql = "insert into relationship (teacher_id,class_id) values ({},{})".format(id, int(item))
            db.commit(relationsql)
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))


def edit_teacherclass(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        sql = "SELECT id,name FROM teacher where id={};".format(nid)
        teacher_info = db.findone(sql)
        sql = "select class_id from relationship where teacher_id = {};".format(nid)
        class_info = db.findmany(sql)
        sql = "select id,title from class;"
        all_class_info = db.findmany(sql)
        class_id = []
        for i in class_info:
            class_id.append(i['class_id'])
        return render(request, 'edit_teacher.html',
                      {"teacher_info": teacher_info, "class_info": class_id, "all_class_info": all_class_info})
    else:
        nid = request.GET.get("nid")
        name = request.POST.get("name")
        class_ids = request.POST.getlist("class_ids")
        # 更新老师表
        sql = "update teacher set name = ('{}') where id = {};".format(name, nid)
        db.commit(sql)
        # 更新老师和班级关系表,先删除所有对应关系然后再添加
        sql = "delete from relationship where teacher_id = {};".format(nid)
        db.commit(sql)
        for item in class_ids:
            relation = "INSERT INTO relationship (teacher_id,class_id) VALUES ({},{})".format(nid, int(item))
            db.commit(relation)
        return redirect("/teachers/")


def get_all_class(request):
    time.sleep(5)
    sql = "select id,title from class;"
    class_list = db.findmany(sql)
    return HttpResponse(json.dumps(class_list))
