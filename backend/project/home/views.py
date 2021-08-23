import json
import re

from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets
from home.models import News, Hots, Collection, Recommend, More, User, donor, donorlink
from home.serializers import NewsSerializer, HotsSerializer, CollectionSerializer, RecommendSerializer, MoreSerializer, UserSerializer, DonorSerializer, DonorlinkSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
import time
from home import models

from django.core.cache import cache  # 存入redis
from rest_framework.response import Response
from project import settings
from random import randint
import hashlib
from .pagination import MyPageNumberPagination

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.core import serializers




class NewsViewSet(viewsets.ModelViewSet):

    queryset = News.objects.all()
    # 使用上一步创建的StudentsSerializer对模型进行序列化
    serializer_class = NewsSerializer
    # permission_classes = (IsAuthenticated,)

class HotsViewSet(viewsets.ModelViewSet):

    queryset = Hots.objects.all()
    # 使用上一步创建的StudentsSerializer对模型进行序列化
    serializer_class = HotsSerializer
    # permission_classes = (IsAuthenticated,)

class CollectionViewSet(viewsets.ModelViewSet):

    queryset = Collection.objects.all()
    # 使用上一步创建的StudentsSerializer对模型进行序列化
    serializer_class = CollectionSerializer
    # permission_classes = (IsAuthenticated,)

class RecommendViewSet(viewsets.ModelViewSet):

    queryset = Recommend.objects.all()
    # 使用上一步创建的StudentsSerializer对模型进行序列化
    serializer_class = RecommendSerializer
    # permission_classes = (IsAuthenticated,)



class MoreViewSet(viewsets.ModelViewSet):

    queryset = More.objects.all()
    # 使用上一步创建的StudentsSerializer对模型进行序列化
    serializer_class = MoreSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = MyPageNumberPagination   #分页设置

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    # 使用上一步创建的StudentsSerializer对模型进行序列化
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

class DonorViewSet(viewsets.ModelViewSet):

    queryset = donor.objects.all()
    # 使用上一步创建的StudentsSerializer对模型进行序列化
    serializer_class = DonorSerializer
    # permission_classes = (IsAuthenticated,)
    pagination_class = MyPageNumberPagination   #分页设置

# class DonorlinkViewSet(viewsets.ModelViewSet):
#
#     queryset = donorlink.objects.all()
#     # 使用上一步创建的StudentsSerializer对模型进行序列化
#     serializer_class = DonorlinkSerializer
#     # permission_classes = (IsAuthenticated,)


# 登录
class AuthView(APIView):

    def post(self,request,*args,**kwargs):

        ret = {'code':1000,'msg':None}
        try:
            # 参数是datadict 形式
            usr = request.data.get('username')
            pas = request.data.get('password')

            # usr = request._request.POST.get('username')
            # pas = request._request.POST.get('password')

            # usr = request.POST.get('username')
            # pas = request.POST.get('password')

            print(usr)
            # obj = models.User.objects.filter(username='yang', password='123456').first()
            obj = models.User.objects.filter(username=usr,password=md5_md5(pas)).first()
            print(obj)
            print(type(obj))
            print(obj.username)
            print(obj.password)
            if not obj:
                ret['code'] = '1001'
                ret['msg'] = '用户名或者密码错误'
                return JsonResponse(ret)
                # 里为了简单，应该是进行加密，再加上其他参数
            token = usr+"25"+oops_oops(pas)
            print(token)
            models.userToken.objects.update_or_create(username=obj, defaults={'token': token})
            ret['msg'] = '登录成功'
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1500
            ret['msg'] = '用户名或者密码错误'
        return JsonResponse(ret)


#搜索结果信息视图
class SearchView(APIView):
    def post(self, request, *args, **kwargs):
        search = request.data['search']
        print(search)
        search_obj = serializers.serialize("json", More.objects.filter(name__icontains=search))
        # search_obj2 = serializers.serialize("json", donor.objects.filter(name__icontains=search))
        ret['data'] = json.loads(search_obj)
        # ret['data2'] = json.loads(search_obj2)  暂时先不加donor里面资源因为 搜索出来会导致donor里面的id和more里面的id一直跳转同一个下载页
        return JsonResponse(ret['data'],safe=False)





ret = {
    'code':'',
    'msg':'',
    'data':{
        'id':'',
        'username':'',
        'password':'',
        'email':''
    }
}


#身份验证2
class AuthticationView2(BaseAuthentication):
    def authenticate(self, request):
        token = request.data['token']
        id = request.data['linknum']
        print(token)
        # 拿到token在数据库匹配
        token_obj = models.userToken.objects.filter(token=token).first()
        global ids
        global token_id2
        ids = id
        token_ = re.split('25',str(token))  #把有%的进行分隔
        token_id2 = token_[0] #把分隔后的数据定义为全局变量 传给视图
        obj = models.User.objects.filter(username=token_id2,isdonor="捐赠者").first()
        if not obj:
            raise exceptions.AuthenticationFailed('权限禁止')
        return (obj.username, obj)

    def authenticate_header(self, request):
        pass

#权限链接信息视图
class DonorlinkAuthView(APIView):
    authentication_classes = [AuthticationView2,] #添加身份验证
    def post(self, request, *args, **kwargs):
        ret = {'code':1000, 'msg':"登录成功"}
        try:
            ret['data'] = serializers.serialize("json", donorlink.objects.filter(pk=ids))
            ret['data'] = json.loads(ret['data'])
            return JsonResponse(ret)
        except Exception as e:
            pass
        return JsonResponse(ret)




#身份验证
class AuthticationView(BaseAuthentication):
    def authenticate(self, request):
        token = request.data['token']
        print(token)
        # 拿到token在数据库匹配
        token_obj = models.userToken.objects.filter(token=token).first()
        global token_id
        token_ = re.split('25',str(token))  #把有%的进行分隔
        token_id = token_[0] #把分隔后的数据定义为全局变量 传给视图
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户登录失败')
        return (token_obj.username, token_obj)

    def authenticate_header(self, request):
        pass

#用户信息视图
class TokenAuthView(APIView):
    authentication_classes = [AuthticationView,] #添加身份验证
    def post(self, request, *args, **kwargs):
        ret = {'code':1000, 'msg':"登录成功"}
        try:
            ret['data'] = serializers.serialize("json", User.objects.filter(username=token_id))
            ret['data'] = json.loads(ret['data'])
            return JsonResponse(ret)
        except Exception as e:
            pass
        return JsonResponse(ret)




# 自定义加密
def oops_oops(params):
    oops = ''
    oopss = ''
    oops_str_1 = ''
    oops_str_2 = ''
    oops_str = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for k in range(10):
        oopss += oops_str[randint(0, 35)]
    oops_str_1 = oopss[0:5]
    oops_str_2 = oopss[5:10]
    oops = oops_str_1 + params + oops_str_2
    return oops

#生成随机的验证码
def Email_Code():
     code_ = ''
     code_str = 'abcdefghijklmnopqrstuvwxyz1234567890'
     for k in range(5):
         code_ += code_str[randint(0,35)]
     return code_

#   md5加盐
def md5_md5(params):
     md5 = hashlib.md5(params.encode(encoding='utf-8'))
     return md5.hexdigest()

class RegisterView(APIView):
 def post(self, request):
     try:
         email = request.data.get('email')  # 获取前端邮箱
         username = request.data.get('username')
         password = request.data.get('password')
         code = request.data.get('vfcode') #获取前段的验证码
         # 验证邮箱的格式
         re_email = r'(\w+)@(\w+)\.(\w+)'
         if not re.match(re_email, email):
             return Response({'code': 1001, 'msg': '邮箱格式不正确'})
         #判断是否输入了验证码
         if not code:
             return Response({'code':1002,'msg':'请输入验证码'})
         #获取验证码，并判断是否失效了
         code_ = cache.get('syl_'+email)
         if not code_:
             return Response({'code':1003,'msg':'验证码已失效'})
         #判断输入的验证码，和获取到的验证码是否一致
         if code == code_:
             data = {
                 'email':email,
                 'password':md5_md5(password),
                 'username':username,
             }
             #   序列化写入数据
             userser = UserSerializer(data=data)
             if not userser.is_valid():
                 return Response({'code':1004,'msg':'用户已存在'})
             ret = {
                 'code': 1000,
                 'msg': '注册成功'
             }
             userser.save()   #提交
             return Response(ret)

         return Response({'code':1005,'msg':'验证码错误'})
     #返回错误信息
     except:
         return Response({'code': 1500, 'msg': '网络有些问题，请等一下再试'})


# post请求
# 获取到验证码，并存入redis
# 发生邮箱
class Email_code_APIView(APIView):
 def post(self, request):
     try:
         # 从前端获取邮箱
         email = request.data.get('email')
         # 生成随机的验证码
         code = Email_Code()
         ret = '【OOPS】{};你好,\n您的验证码是:{}\n此验证码仅用于注册OOPS账号,有效期3分钟'.format(email,code)
        # 给邮箱发送验证码
         my_email = send_mail('OOPS验证码', ret, settings.DEFAULT_FROM_EMAIL, [email])
         if not my_email == 1:
             return Response({
                 'code': 1006,
                 'msg': "邮件发送失败",
             })
         key = 'syl_' + email
         cache.set(key, code, 30)  # 5分钟的有效时间
         ret = {
             'code': 1000,
             'msg': "邮件发送成功"
         }
         return Response(ret)
     # 返回错误信息
     except:
         return Response({'code': 1500, 'msg': '网络有些问题，请等一下再试'})




#找回密码
# 获取到验证码，并存入redis
# 发生邮箱
class Forget_Email_code_APIView(APIView):
 def post(self, request):
     ret = {'code': 1000, 'msg': None}
     try:
         # 从前端获取邮箱
         email = request.data.get('email')
         username = request.data.get('username')
         same = models.User.objects.filter(username=username,email=email).first()
         if not same:
             ret['code'] = '1010'
             ret['msg'] = '账号与邮箱不匹配'
             return JsonResponse(ret)
         # 生成随机的验证码
         code = Email_Code()
         ret = '【OOPS】{};你好,\n您的验证码是:{}\n此验证码仅用于找回OOPS密码,有效期3分钟'.format(email,code)
        # 给邮箱发送验证码
         my_email = send_mail('OOPS验证码', ret, settings.DEFAULT_FROM_EMAIL, [email])
         if not my_email == 1:
             return Response({
                 'code': 1006,
                 'msg': "邮件发送失败",
             })
         key = 'syl_' + email
         cache.set(key, code, 30)  # 5分钟的有效时间
         ret = {
             'code': 1000,
             'msg': "邮件发送成功"
         }
         return Response(ret)
     # 返回错误信息
     except:
         return Response({'code': 1500, 'msg': '网络有些问题，请等一下再试'})


class ForgetView(APIView):
 def post(self, request):
     try:
         email = request.data.get('email')  # 获取前端邮箱
         username = request.data.get('username')
         password = request.data.get('password')
         code = request.data.get('vfcode') #获取前段的验证码
         # 验证邮箱的格式
         re_email = r'(\w+)@(\w+)\.(\w+)'
         if not re.match(re_email, email):
             return Response({'code': 1001, 'msg': '邮箱格式不正确'})
         #判断是否输入了验证码
         if not code:
             return Response({'code':1002,'msg':'请输入验证码'})
         #获取验证码，并判断是否失效了
         code_ = cache.get('syl_'+email)
         if not code_:
             return Response({'code':1003,'msg':'验证码已失效'})
         #判断输入的验证码，和获取到的验证码是否一致
         if code == code_:
             data = {
                 'email': email,
                 'password': md5_md5(password),
                 'username': username,
             }
             obj = models.User.objects.filter(username=username, email=email).first()
             obj.password = md5_md5(password)
             ret = {
                 'code': 1000,
                 'msg': '密码更改成功'
             }
             obj.save()  # 提交
             return Response(ret)

         return Response({'code': 1005, 'msg': '验证码错误'})
     #返回错误信息
     except:
         return Response({'code': 1500, 'msg': '网络有些问题，请等一下再试'})