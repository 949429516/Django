from django.shortcuts import render, redirect
import pymysql

def classes(request):
    conn = pymysql.connect(host= "localhost", port= 3306, user= "root",
                           password= "19950811", database= "oldboy",
                           charset= "utf8")
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
        conn = pymysql.connect(host="localhost", port=3306, user="root",
                               password="19950811", database="oldboy",
                               charset="utf8")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql_find = "insert into class (title) values ('{}');".format(value)
        print(sql_find)
        try:
            cursor.execute(sql_find)
            conn.commit()
        except:
            conn.rollback()
        cursor.close()
        conn.close()
        return redirect('/classes/')


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