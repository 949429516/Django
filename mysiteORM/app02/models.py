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
    # ManyToManyField第二种方法可以指定表,但是只有查询和清空的功能
    # m = models.ManyToManyField('Gril',through='Love',through_fields=('boy','gril',))
    # obj = models.Boy.objects.filter(name='xxx').first()
    # 增加obj.m.add(2) obj.m.add(*[4,]) 重置obj.m.set(2) 删除obj.m.remove(2) 有关的删除obj.m.clear()
    # 关联表的对象gril_list = obj.m.all()
    # 反向关联obj = models.Gril.objects.filter(name='xxx').first()
    # v = obj.boy_set.all()
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
