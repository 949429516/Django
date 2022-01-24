from django.db import models


# Create your models here.

class Foo(models.Model):
    caption = models.CharField(max_length=16)


class UserType(models.Model):
    """
    用户类型
    """
    title = models.CharField(max_length=32)
    # fo = models.ForeignKey('Foo', on_delete=models.CASCADE)


class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    ut = models.ForeignKey('UserType', on_delete=models.CASCADE)

    def __str__(self):
        return "%s-%s" % (self.id, self.name)


class Boy(models.Model):
    name = models.CharField(max_length=32)
    # django可以协助你新建一个关联表
    # m = models.ManyToManyField('Gril')

class Gril(models.Model):
    name = models.CharField(max_length=32)
    # m = models.ManyToManyField('Boy')



class Love(models.Model):
    boy = models.ForeignKey('Boy', on_delete=True)
    gril = models.ForeignKey('Gril', on_delete=True)

    class Meta:
        # 联合唯一索引
        unique_together = [
            ('boy', 'gril')
        ]
