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
            L = []
            data = data_list.pop()
            L.append(data['title'])
            tid = data['tid']
            if tid in visted:
                data_list.pop()
                continue
            visted.append(tid)
            for i in data_list:
                if i['tid'] == tid:
                    L.append(i['title'])
            data['title'] = L
            teacherclass_list.append(data)
        print(teacherclass_list)
        return render(request, 'teacherclass.html', {'teachers_list': teacherclass_list})
    else:
        pass