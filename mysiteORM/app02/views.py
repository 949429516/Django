from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from utils.pager import PageInfo
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
    return render(request, 'custom.html', {'user_list': user_list, 'pageinfo': pageinfo})
