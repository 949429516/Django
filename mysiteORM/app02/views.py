from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from utils.pager import PageInfo
from django.db.models import Count

from app02 import models


def test(request):
    # 创建数据 返回值就是增加的数据,create每次都会提交一次
    # models.UserType.objects.create(title="普通用户")
    # models.UserType.objects.create(title="二逼用户")
    # models.UserType.objects.create(title="牛逼用户")
    # models.UserInfo.objects.create(name='王森鲍', age=30, ut_id=1)
    # models.UserInfo.objects.create(name='王小雅', age=21, ut_id=2)
    # models.UserInfo.objects.create(name='李沁园', age=31, ut_id=2)
    # models.UserInfo.objects.create(name='陈昊', age=29, ut_id=3)
    # models.UserInfo.objects.create(name='吴瑶', age=24, ut_id=2)
    # obj = models.UserInfo.objects.create(**{'title': 'xxx'})

    # 如果批量增加直接使用create会频繁写入数据库，造成数据库的性能下降用下面的方法统一提交
    # obj = models.UserType(title='xx')#这时候还未提交
    # obj.save()#保存

    # objs = [
    #     models.UserType(name='r11'),
    # ]
    # models.UserType.objects.bulk_create(objs, 10)#每次提交10条,不要超过999

    # get_or_create如果存在则获取，否则创建;defaults创建时其他字段的值,返回obj=获取到的对象 create=True False
    # update_or_create如果存在则更新，否则创建;defaults创建时其他字段的值
    # obj, created = models.UserInfo.objects.get_or_create(username='root1', defaults={'email': 'xxx@qq.com', 'ut_id': 2})

    # 获取 正向操作
    # QuerySet[obj,obj,obj]
    # result = models.UserInfo.objects.all()
    # for obj in result:
    #     print(obj.name, obj.age, obj.ut.title)

    # only 只获取
    # models.UserInfo.objects.all().only('ut_id', 'name')

    # defer 除了name其他都获取
    # models.UserInfo.objects.all().defer('name')

    # dates

    # datetimes

    # get获取一个 找不到或者多个抛出异常，fitst找不到返回None
    # models.UserInfo.objects.get(id=1)

    # 外键 反向操作 表名小写_set.all()
    # obj = models.UserType.objects.all().first()
    # print(f'用户类型{obj.id}{obj.title}')
    # for row in obj.userinfo_set.all():
    #     print(row.name, row.age)

    # 连表查询,使用连表会使性能下降.但是,ForeignKey约束，节省空间
    # result = models.UserType.objects.all()
    # for item in result:
    #     print(item.title, item.userinfo_set.filter(name="xx"))

    # select_related以上的操作每次for循环会使用外键查询都会再次访问数据库造成性能下降，如果连表推进下面的方法
    # select * from userinfo inner join usertype on userinfo.ut = usertype.id
    # result = models.UserInfo.objects.all().select_related('ut')

    # prefetch_related实际上是两次单表查询
    # result = models.UserInfo.objects.all().prefetch_related('ut')
    # Django查询了两次表，第一次查询外键表，第二次使用查询的结果查询外键关联的表，最终整合
    # select * from userinfo; Django内部 ut_id = [2,4]; select * from usertype where id in [2,4];
    # for row in result:
    #    print(row.id, row.ut.title)

    # values取值 循环时无法跨表,只有在获取的时候跨表
    # values跨表
    # result = models.UserInfo.objects.all().values('id', 'name', 'ut__title')
    # QuerySet[{'id':'xxx','name':'xxx'}] values('id', 'name')
    # QuerySet[(1,'f'),()] values_list('id', 'name')

    # 排序
    # result = models.UserInfo.objects.all().order_by('id')

    # 分组聚合
    # from django.db.models import Count, Sum, Min
    # v = models.UserInfo.objects.values('ut_id').annotate(xxx=Count('id'))
    # print(v.query)
    # having
    # v = models.UserInfo.objects.values('ut_id').annotate(xxx=Count('id')).filter(xxx__gt=2)
    # print(v.query)

    # aggreate整张表聚合
    # result = models.UserInfo.objects.aggregate(k=Count('ut_id', distinct=True), n=Count('id'))
    # print(result)

    # 去重复distinct
    # models.UserInfo.objects.values('ut_id').distinct()#mysql
    # select distinct ut_id from userinfo;
    # models.UserInfo.objects.distinct('ut_id')#postgresql

    # models.UserInfo.objects.filter(id__gt=1)
    # models.UserInfo.objects.filter(id__in=[1, 2, 3])#在这些之中
    # models.UserInfo.objects.filter(age__isnull=True) #判断为空
    # models.UserInfo.objects.in_bulk([1, 2, 3]) #id_in的简便写法

    # models.UserInfo.objects.filter(id__range=[1, 2])#范围内
    # models.UserInfo.objects.filter(name__startwith='xxx')#以开头
    # models.UserInfo.objects.filter(name__contains='xxx')#包含
    # models.UserInfo.objects.exclude(id=1)# 不等于

    # F Q  F用于操作字段更新时取到原来的值 Q一般用于组合查询（复杂情况下）
    #     from django.db.models import F, Q
    #     models.UserInfo.objects.all().update(age=F("age") + 1)
    #
    #     condition = {'id': 1, 'name': 'root'}
    #     models.UserInfo.objects.filter(**condition)
    #     # Q对象的方式
    #     models.UserInfo.objects.filter(Q(id__gt=1) | Q(id=10))  # id>1或者id=10
    #     models.UserInfo.objects.filter(Q(id=1) & Q(id=10))  # id=1并且id=10
    #     # Q方法的方式
    #     q1 = Q()
    #     q1.connector = "OR"
    #     q1.children.append(('id', 1))
    #     q1.children.append(('id', 10))
    #     q1.children.append(('id', 9))
    #     q2 = Q()
    #     q2.connector = "OR"
    #     q2.children.append(('c1', 1))
    #     q2.children.append(('c1', 10))
    #     q2.children.append(('c1', 9))
    #     con = Q()
    #     con.add(q1, 'AND')
    #     con.add(q2, 'AND')
    #     # 相当于(id=1 or id = 10 or id =9) and (c1=1 or c1=10 or c1=9)
    #     condition_dict = {
    #         'k1': [1, 2, 3, 4],
    #         'k2': [1, ],
    #     }
    #     con = Q()
    #     for k, v in condition_dict:
    #         q = Q()
    #         q.connector = 'OR'
    #         for i in v:
    #             q.children.append('id', i)
    #         con.add(q, 'AND')
    #     models.UserInfo.objects.filter(con)
    #     # extra额外的查询条件
    #     # select id,name,(select count(1) from tb) as n from xb
    #     v = models.UserInfo.objects.all().extra(select={'n': 'select count(1) from app02_usertype where id>%s',
    #                                                     'm': 'select count(1) from app02_usertype where id>%s'},
    #                                             select_params=[1, 2])
    #     for obj in v:
    #         print(obj.name, obj.id, obj.n)
    #     # 可以写原生的sql语句中间是and连接
    #     models.UserInfo.objects.extra(
    #         where=["id=1 or id=2", "name='alex'"]
    #     )
    #     # 多长表查询 select * from app01_userinfo,app01_usertype where app01_usertype.id=app01_userinfo.ut_id
    #     models.UserInfo.objects.extra(
    #         tables=['app01_usertype'],
    #         where=['app01_usertype.id=app01_userinfo.ut_id']
    #     )
    #     # extra综合
    #     models.UserInfo.objects.extra(
    #         select={'newid': 'select count(1) from app02_usertype where id>%s'},
    #         select_params=[1, ],
    #         where=['age>%s'],
    #         params=[18, ],
    #         order_by=['-age'],
    #         tables=['app01_usertype']
    #     )
    #     """
    #     select
    #         app02_userinfo.id,
    #     (select count(1) from app02_usertype where id>1) as newid
    #     from
    #         app02_userinfo,app02_usertype
    #     where
    #         app02_userinfo.age>18
    #     order by
    #         app02_userinfo.age desc;
    #     """
    #
    #     # using 指定在哪个数据库获取数据
    #     models.UserInfo.objects.all().using('db2')
    #
    #
    #     # 原生sql
    #     from django.db import connection, connections
    #     cursor = connection.cursor()
    #     # 连接不同数据库用connections在setting配置的数据库名
    #     cursors = connections['default'].cursor()
    #     cursor.execute('select * from app02_userinfo')
    #     row = cursor.fetchone()
    #
    #
    #     # 原生sql---raw
    #     models.UserInfo.objects.raw('select * from app02_userinfo')
    #     # 这样写有可能会报错，原因是userinfo对象中可能没有usertype的列名,解决方法设置别名或(select id as ut_id)者前后同为一张表
    #     models.UserInfo.objects.raw('select * from app02_usertype')
    #     # 设置别名方法2
    #     name_map = {'fitst': 'first_name', 'list': 'list_name'}
    #     models.UserType.objects.raw('select * from app02_userinfo', translations=name_map)
    #
    # 多对多
    # objs = [
    #     models.Boy(name="李沁岩"),
    #     models.Boy(name="王森宝"),
    #     models.Boy(name="陈昊"),
    #     models.Boy(name="赵恒"),
    # ]
    # models.Boy.objects.bulk_create(objs, 5)
    # obj = [
    #     models.Boy(name="吴瑶"),
    #     models.Boy(name="郭成凤"),
    #     models.Boy(name="王玺"),
    #     models.Boy(name="王小雅"),
    # ]
    # models.Gril.objects.bulk_create(obj, 5)
    # models.Love.objects.create(boy_id=1, gril_id=1)
    # models.Love.objects.create(boy_id=1, gril_id=4)
    # models.Love.objects.create(boy_id=2, gril_id=4)
    # models.Love.objects.create(boy_id=2, gril_id=2)
    # 1.查找与李沁岩有关系的姑娘
    # obj = models.Boy.objects.filter(name='李沁岩').first()
    # love_list = obj.love_set.all()
    # for row in love_list:
    #     print(row.gril.name)

    # love_list = models.Love.objects.filter(boy_id__name="李沁岩")
    # for row in love_list:
    #     print(row.gril.name)

    # 上面的方法每次for循环都会去查询一次数据库
    # love_list = models.Love.objects.filter(boy_id__name="李沁岩").values("gril__name")
    # for row in love_list:
    #     print(row["gril__name"])

    # love_list = models.Love.objects.filter(boy_id__name="李沁岩").select_related('gril')
    # for obj in love_list:
    #     print(obj.gril.name)
    love_list = models.Love.objects.filter(boy_id__name="李沁岩")
    print(love_list.query)
    return HttpResponse('...')


def index(request):
    """
    分页
    :param request:
    :return:
    """
    # for i in range(300):d
    #     name = "root" + str(i)
    #     age = 18
    #     ut = 1
    #     models.UserInfo.objects.create(name=name, age=age, ut_id=ut)
    current_page = request.GET.get('page')
    user_list = models.UserInfo.objects.all()
    '''分页对象
    per_page:每页显示条目数量
    count: 数据总个数
    num_pages:总页数
    page_range:总页数的索引范围，如：（1,10）(1,200)
    page: page对象当前显示第几页'''
    paginator = Paginator(user_list, 10)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e:
        posts = paginator.page(1)
    '''has_next 是否有下一页
    has_previous 是否有上一页
    next_page_number 下一页页码
    previous_page_number 下一页页码
    object_list 分页之后的数据列表
    number 当前页
    paginator paginator对象
    '''
    return render(request, 'index1.html', {'posts': posts})


def custom(request):
    # 表示用户想要访问的页码
    all_count = models.UserInfo.objects.all().count()
    current_page = request.GET.get('page')
    # 每页显示的数据个数
    pageinfo = PageInfo(current_page, all_count, 10, 5, 'custom')
    start = pageinfo.start()
    end = pageinfo.end()
    user_list = models.UserInfo.objects.all()[start:end]
    # django中也有安全标签 xss攻击慎用 safe和mark_safe
    # from django.utils.safestring import mark_safe
    # user_list = mark_safe(user_list)
    return render(request, 'custom.html', {'user_list': user_list, 'pageinfo': pageinfo})
