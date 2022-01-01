from django.shortcuts import render, HttpResponse
from django.urls import reverse
from app01 import models
from django.views import View


# Create your views here.

def index(request, a1):
    """
    反向生成url
    kwargs需要参数名一致
    :param request:
    :param a1:
    :return:
    """
    user_list = ['wsb', 'alex', 'djb']
    # v = reverse('name1', kwargs={'a1': 11111})
    v = reverse('name1', kwargs={'a1': a1})
    print(a1)
    print(v)
    return render(request, 'index.html', {"user_list": user_list})


# r'^edit/(\w+)/        edit(request,a1):
# r'^edit/(\w+)/(\w+)/  edit(request,a1,a2): 需要严格按顺序获取
# r'^edit/(?P<a1>\w+)/(?P<a2>\w+)/ 正则分组，给参数命名
def edit(request, a1):
    print(a1)
    return HttpResponse("...")


def login(request):
    return render(request, 'login.html')


# 数据库相关操作
def index1(request):
    # 增删改查
    """新增"""
    # models.UserGroup.objects.create(title='销售部')
    # models.UserInfo.objects.create(username='王森鲍', age=38, passwd='123456', ug_id=1)
    """查询 QuerySet类型（列表）"""
    # group_lits = models.UserGroup.objects.all()
    # group_lits = models.UserGroup.objects.filter(id=1)
    # group_lits = models.UserGroup.objects.filter(id__gt=1)
    # group_lits = models.UserGroup.objects.filter(id__li=1)
    """删除"""
    # models.UserGroup.objects.filter(id=2).delete()
    """改"""
    models.UserGroup.objects.filter(id=2).update(title='公关部')
    group_lits = models.UserGroup.objects.all()
    print(group_lits)
    for row in group_lits:
        print(row.id, row.title)
    models.UserInfo.objects.all()
    return render(request, 'newindex.html', {'group_lits': group_lits})


class Login(View):
    """
    CBV方式需要继承View类，可以在类中用函数区分
    get     查询
    post    创建
    put     更新
    delete  删除
    """

    # 调用父类方法
    def dispatch(self, request, *args, **kwargs):
        # 这里类似于装饰器
        print("before")
        obj = super(Login, self).dispatch(request, *args, **kwargs)
        print("after")
        return obj

    def get(self, request):
        return render(request, 'CBVLogin.html')

    def post(self, request):
        print(request.POST.get('user'))
        return HttpResponse("login.post")
