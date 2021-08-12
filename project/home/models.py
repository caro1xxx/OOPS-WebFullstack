from django.db import models
import time

class News(models.Model):
    name = models.TextField(verbose_name='名称')
    content = models.TextField(verbose_name='内容')
    auth = models.TextField(verbose_name='作者')
    create_data = models.DateField(auto_now=True, verbose_name='更新时间')

class Hots(models.Model):
    name = models.TextField(verbose_name='名称')
    content = models.TextField(verbose_name='内容')
    auth = models.TextField(verbose_name='作者')
    create_data = models.DateField(auto_now=True, verbose_name='更新时间')

class Collection(models.Model):
    name = models.TextField(verbose_name='名称')
    content = models.TextField(verbose_name='内容')
    auth = models.TextField(verbose_name='作者')
    create_data = models.DateField(auto_now=True, verbose_name='更新时间')



class Recommend(models.Model):
    name = models.TextField(verbose_name='名称')
    content = models.TextField(verbose_name='内容')
    auth = models.TextField(verbose_name='作者')
    create_data = models.DateField(auto_now=True, verbose_name='更新时间')



class More(models.Model):
    name = models.TextField(verbose_name='名字')
    introduce = models.TextField(verbose_name='介绍')
    size = models.TextField(verbose_name='大小')
    version = models.TextField(verbose_name='版本')
    content = models.TextField(verbose_name='内容')
    link = models.TextField(verbose_name='链接')
    create_data = models.DateField(auto_now=True, verbose_name='更新时间')
    isshow = models.TextField(verbose_name='是否显示')
    # code = models.TextField(verbose_name='提取码') 项目新添代码


class User(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=64,unique=True)
    isdonor = models.CharField(max_length=32, default="非捐赠者")
    create_time = models.DateField(auto_now=True)
    money = models.IntegerField(default=0)

    class Meta:
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户信息表'

class userToken(models.Model):
    username = models.OneToOneField(to='User',on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=64)

    class Meta:
        db_table =  'user_token'
        verbose_name = verbose_name_plural = '用户token表'


class donor(models.Model):
    name = models.CharField(max_length=64, verbose_name='名字')
    introduce = models.TextField(verbose_name='介绍')
    size = models.TextField(verbose_name='大小')
    version = models.TextField(verbose_name='版本')
    content = models.TextField(verbose_name='内容')
    create_data = models.DateField(auto_now=True, verbose_name='更新时间')
    # icon = models.TextField(verbose_name='图标') 项目新添代码

class donorlink(models.Model):
    link = models.TextField(verbose_name='链接')
    # code = models.TextField(verbose_name='提取码') 项目新添代码