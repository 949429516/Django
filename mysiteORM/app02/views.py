from django.shortcuts import render, HttpResponse

# Create your views here.

from app02 import models


def test(request):
    # 创建数据
    # models.UserType.objects.create(title="普通用户")
    # models.UserType.objects.create(title="二逼用户")
    # models.UserType.objects.create(title="牛逼用户")
    # models.UserInfo.objects.create(name='王森鲍', age=30, ut_id=1)
    # models.UserInfo.objects.create(name='王小雅', age=21, ut_id=2)
    # models.UserInfo.objects.create(name='李沁园', age=31, ut_id=2)
    # models.UserInfo.objects.create(name='陈昊', age=29, ut_id=3)
    # models.UserInfo.objects.create(name='吴瑶', age=24, ut_id=2)

    # 获取 正向操作
    # QuerySet[obj,obj,obj]
    # result = models.UserInfo.objects.all()
    # for obj in result:
    #     print(obj.name, obj.age, obj.ut.title)

    # 外键 反向操作 表名小写_set.all()
    # obj = models.UserType.objects.all().first()
    # print(f'用户类型{obj.id}{obj.title}')
    # for row in obj.userinfo_set.all():
    #     print(row.name, row.age)

    # 连表查询
    # result = models.UserType.objects.all()
    # for item in result:
    #     print(item.title, item.userinfo_set.filter(name="xx"))

    # values取值 循环时无法跨表,只有在获取的时候跨表
    # values跨表
    # result = models.UserInfo.objects.all().values('id', 'name', 'ut__title')
    # QuerySet[{'id':'xxx','name':'xxx'}] values('id', 'name')
    # QuerySet[(1,'f'),()] values_list('id', 'name')
    result = models.UserInfo.objects.all().values('id', 'name')
    for row in result:
        print(row)
    return HttpResponse("...")
