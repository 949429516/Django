from django.shortcuts import HttpResponse, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator


# 全局打开后局部禁用csrf加上csrf_exempt该装饰器
# 全局禁用后局部使用加上csrf_protect该装饰器
@csrf_protect
def csrf1(request):
    if request.method == "GET":
        return render(request, 'csrf.html')
    else:
        return HttpResponse("OK")


# 为所有请求添加
"""
CBV中加装饰器的三种方式	装饰器csrf_protect	装饰器csrf_exempt
在类中直接加在某个函数上	有效	                无效
在类头顶上给某个函数加	有效	                无效
给dispatch函数加	    有效	                有效"""


@method_decorator(csrf_protect, name='dispatch')
# 为特定请求添加
# @method_decorator(csrf_exempt, name='get')
# @method_decorator(csrf_exempt, name='post')
class Foo(View):

    def get(self, request):
        return render(request, 'csrf.html')

    def post(self, request):
        return HttpResponse("OK")
