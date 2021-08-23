# -*- coding: utf-8 -*-
# @Time    : 2021/7/29 8:29
# @Author  : XobNcaro1xxx
# @File    : serializers.py
# @Software: PyCharm

from rest_framework import serializers
from home.models import News, Collection, Hots, Recommend, More, User, donor, donorlink


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = News
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'

class HotsSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = Hots
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'

class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = Collection
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'

class RecommendSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = Recommend
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'




class MoreSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = More
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = User
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = donor
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'



class DonorlinkSerializer(serializers.ModelSerializer):

    class Meta:
        # 对HomeModel进行序列化
        model = donorlink
        # __all__表示对 HomeModel 中所有字段序列化进行序列化
        fields = '__all__'
