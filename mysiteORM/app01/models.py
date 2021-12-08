from django.db import models


# Create your models here.
class UserGroup(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    nid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=32)
    passwd = models.CharField(max_length=64)
    age = models.IntegerField(default=1)
    ug = models.ForeignKey("UserGroup", on_delete=models.CASCADE, null=True)
