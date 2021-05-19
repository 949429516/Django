from django.shortcuts import render, redirect, HttpResponse
from .SqlManager import dbManager
import pymysql, json

db = dbManager()


def classes(request):
    conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="19950811", database="oldboy",
                           charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql_find = "select id, title from class;"
    try:
        cursor.execute(sql_find)
        class_list = cursor.fetchall()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
    return render(request, 'classes.html', {'class_list': class_list})


def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        value = request.POST.get('title')
        if len(value) > 0:
            sql_find = "insert into class (title) values ('{}');".format(value)
            db.commit(sql_find)
            return redirect('/classes/')
        else:
            return render(request, 'add_class.html', {'msg': '班级名称不能为空'})


# 对话框的提交
def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sql = "insert into class(title) values ('{}')".format(title)
        db.commit(sql)
        return HttpResponse('OK')
    else:
        # 页面不要刷新并且提示错误信息
        return HttpResponse('班级标题不能为空')


def del_class(request):
    nid = request.GET.get("nid")
    conn = pymysql.connect(host="localhost", port=3306, user="root",
                           password="19950811", database="oldboy",
                           charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql_find = "delete from class where id = {};".format(nid)
    print(sql_find)
    try:
        cursor.execute(sql_find)
        conn.commit()
    except:
        conn.rollback()
    cursor.close()
    conn.close()
    return redirect('/classes/')


def modal_del_class(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get("nid")
        name = request.POST.get("name")
        sql = "delete from class where id = {};".format(nid)
        db.commit(sql)
    except Exception as e:
        ret = {'status': False, 'message': "删除%s失败%s" % name % e}
    return HttpResponse(json.dumps(ret))


def edit_class(request):
    if request.method == 'GET':
        nid = request.GET.get("nid")
        conn = pymysql.connect(host="localhost", port=3306, user="root",
                               password="19950811", database="oldboy",
                               charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql_find = "select id, title from class where id = {};".format(nid)
        try:
            cursor.execute(sql_find)
            class_list = cursor.fetchone()
        except:
            conn.rollback()
        cursor.close()
        conn.close()
        return render(request, 'edit_class.html', {'class_list': class_list})
    else:
        nid = request.POST.get("nid")
        title = request.POST.get("title")
        conn = pymysql.connect(host="localhost", port=3306, user="root",
                               password="19950811", database="oldboy",
                               charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql_find = "update class set title = '{}' where id = {};".format(title, nid)
        print(sql_find)
        try:
            cursor.execute(sql_find)
            conn.commit()
        except:
            conn.rollback()
        cursor.close()
        conn.close()
        return redirect('/classes/')


def modal_edit_class(request):
    ret = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        content = request.POST.get('content')
        sql = "update class set title = '{}' where id = {}".format(content, nid)
        db.commit(sql)
    except Exception as e:
        ret['status'] = False
        ret['message'] = e
    return HttpResponse(json.dumps(ret))
