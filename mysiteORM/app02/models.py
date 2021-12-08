from django.db import models


# Create your models here.

class Foo(models.Model):
    caption = models.CharField(max_length=16)


class UserType(models.Model):
    """
    用户类型
    """
    title = models.CharField(max_length=32)
    #fo = models.ForeignKey('Foo', on_delete=models.CASCADE)


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    ut = models.ForeignKey('UserType', on_delete=models.CASCADE)
