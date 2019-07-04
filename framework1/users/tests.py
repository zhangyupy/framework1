import os

from django.test import TestCase

# Create your tests here.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'framework1.settings')
# 让Django进行一次初始化
import django
django.setup()
from rest_framework import serializers
# Create your tests here.


class User(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class UserSerializer(serializers.Serializer):
    name=serializers.CharField()
    age=serializers.IntegerField(read_only=True)
if __name__ == '__main__':
    user=User('里多余',19)
    serializer = UserSerializer(user)  # 创建序列化器类对象
    print(serializer.data)

"""反序列化掩饰"""
print('反序列化操作***********')
if __name__ == '__main__':
    req_data={'name':'itheima','age':6}
    serializer=UserSerializer(data=req_data)  # 创建序列化器类对象
    res=serializer.is_valid() #参数校验，True or False
    print(res)
    res_errors=serializer.errors # 获取校验失败之后错误提示信息
    print(res_errors)
    # 获取检验之后的数据
    res_data=serializer.validated_data
    print(serializer.validated_data)# 获取校验通过之后的数据
    print(res_data)