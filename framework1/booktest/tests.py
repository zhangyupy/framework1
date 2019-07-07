import os
import json
from django.test import TestCase
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "framework1.settings")
import django
django.setup()
# Create your tests here.
from booktest.models import BookInfo, HeroInfo
# 查询获取图书对象
from booktest.serializers import BookinfoSerializer, HeroinfoSerializer

# book = BookInfo.objects.get(id=2)
# 创建序列化器对象
# serializer = BookinfoSerializer(book)

# 获取序列化之后的数据
# print(serializer.data)
"""序列化多个对象"""
# books = BookInfo.objects.all()
# # 创建序列化器对象
# serializer = BookinfoSerializer(books, many=True)
# # 获取序列化之后的数据
# str1=json.dumps(serializer.data,ensure_ascii=False,indent=1)
# print(str1)
"""关联对象的嵌套序列化"""
hero = HeroInfo.objects.get(id=6)
serializer = HeroinfoSerializer(hero)
print(json.dumps(serializer.data,ensure_ascii=False,indent=1))
